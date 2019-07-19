@backend
@user
@get_users

Feature: View all users and by user id

  Scenario: I can view all users
    Given I already have at least one user
    When I do a get all users request
    Then I should receive a 200 response code and an item has the correct attributes

  Scenario: I get the list of users incremented after each new user added
    Given I get the number of existing users
    And I already have a new user
    When I get the number of users
    Then in the end the list of users is larger with one item

  Scenario: I get the user details when I make a request with correct user id
    Given I already have a new user
    When I do a get request for one user with correct user_id
    Then the related user payload is successfully displayed

  Scenario: I get an error when I make a request for user details with a not existing user id
    Given I have an user_id for an user that doesn't exist
    When I do a get request for one user with that user_id
    Then I receive an error that the user was not found
