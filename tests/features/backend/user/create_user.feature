@backend
@user
@create_user

Feature: Create users

  Scenario: I can add an user
    Given I have a correct User payload
    When I do a POST request to the user endpoint
    Then the request will be successful with 200 response code
    And the response will contain the new object with the related ID

  Scenario: I cannot add several users with the same email
    Given I add a new user
    When I try to add another user with the same email address
    Then I receive an error that the email address already exists

  Scenario: I cannot add a new user without its first name
    Given I have an User payload without first_name
    When I do a POST request to the user endpoint
    Then I receive an error that the first_name is required

  Scenario: I cannot add a new user without its last name
    Given I have an User payload without last_name
    When I do a POST request to the user endpoint
    Then I receive an error that the last_name is required

  Scenario: I cannot add a new user without its email
    Given I have an User payload without email
    When I do a POST request to the user endpoint
    Then I receive an error that the email is required

  Scenario: I cannot add a new user with invalid email format
    Given I have an User payload with invalid email format
    When I do a POST request to the user endpoint
    Then I receive an error that the email is invalid
