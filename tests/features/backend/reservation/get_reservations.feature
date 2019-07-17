@backend
@reservation
@get_reservations

Feature: Get reservations

  Scenario: I can view all reservations
    Given I have at least one reservation added into database
    When I do a get all reservations request
    Then I should receive a 200 response code and a reservation has the correct attributes

  @mda
  Scenario: I can get the details of a reservation using the book_id
    Given I have at least one reservation added into database
    When I do a get request for reservation using book id
    Then I get the correct details of that reservation

  Scenario: I can get the details of a reservation using the user_id and book_id
    Given I have at least one reservation added into database
    When I do the get request for reservation using user_id and book id
    Then I get the correct details of that reservation

  Scenario: I can get the details of all reservations that a user has in database using his user_id
    Given I have at least one reservation added into database
    And I add a new reservation for the same user
    When I do a get request for reservation using user id
    Then I get the details of all reservations that a user has in database
