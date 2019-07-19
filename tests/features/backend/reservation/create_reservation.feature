@backend
@reservation
@create_reservation

Feature: Create reservations

  Scenario: I can successfully create a reservation
    Given I already have an user and a book
    And I have a valid payload to create a reservation
    When I do a POST request to the reservation endpoint
    Then the request will be successful with 200 response code
    And the response will contain the new reservation with the correct details

  Scenario: I cannot create more than one reservation with the same details
    Given I already have an user and a book
    And I have a valid payload to create a reservation
    When I do a POST request to the reservation endpoint
    And I try to create another reservation with the same details
    Then I get an error that the reservation already exists
