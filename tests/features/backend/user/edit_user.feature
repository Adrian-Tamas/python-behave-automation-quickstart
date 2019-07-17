@backend
@user
@edit_user

Feature: Edit user details

  Scenario: I can successfully change an user details
    Given I have a new user added into database
    And I want to change the first and last name
    When I do a PUT request to the user endpoint
    Then the response is with success and the updated user details are displayed

  Scenario: I cannot change the email address for an existing user
    Given I have a new user added into database
    And I want to assign a new email address to that user
    When I do a PUT request to the user endpoint
    Then I receive the error that the email address is invalid and the user details will not be updated
