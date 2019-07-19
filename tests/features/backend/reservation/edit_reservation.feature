@backend
@reservation
@edit_reservation

Feature: Edit reservations

  Scenario: I can successfully edit a reservation
    Given I already have at least one reservation
    And I want to change the reservation dates
    When I do a PUT request to the reservation endpoint
    Then the response is with success and the updated reservation details are displayed

  Scenario: I cannot edit a reservation using not existing user_id
    Given I already have at least one reservation
    And I want to change the reservation dates using not existing user_id
    When I do a PUT request to the reservation endpoint
    Then I get an error that the reservation that I want to edit is invalid

  Scenario: I cannot edit a reservation using not existing book_id
    Given I already have at least one reservation
    And I want to change the reservation dates using not existing book_id
    When I do a PUT request to the reservation endpoint
    Then I get an error that the reservation that I want to edit is invalid
