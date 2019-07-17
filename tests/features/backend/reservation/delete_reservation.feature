@backend
@reservation
@delete_reservation

Feature: Delete reservation

  Scenario: I can delete a reservation using the book_id
    Given I have at least one reservation added into database
    When I do a delete request for reservation using book id
    Then I successfully deleted the reservation from database

  Scenario: I can delete a reservation using the user_id
    Given I have at least one reservation added into database
    When I do a delete request for reservation using user id
    Then I successfully deleted reservation for user from database

  Scenario: I cannot delete a reservation using not existing book_id
    Given I added a user into database
    When I try to delete reservation using wrong book id
    Then I get an error that the reservation wasn't found

  Scenario: I cannot delete a reservation using not existing user_id
    Given I added a user into database
    When I try to delete reservation using wrong book id
    Then I get an error that the reservation wasn't found
