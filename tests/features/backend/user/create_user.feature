@backend
@user
@create_user

Feature: Create users

  Scenario: I can add an user to database
    Given I have a correct User configuration
    When I do a POST request to the user endpoint
    Then the request will be successful with 200 response code
    And the response will contain the new object with the related ID

  Scenario: I cannot add several users with the same email
    Given I have a new user added into database
    When I try to add another user with the same email address
    Then I receive an error that the email address already exists

  Scenario: I cannot add a new user without his first name
    Given I have an User configuration without first_name
    When I do a POST request to the user endpoint
    Then I receive an error that the first_name is required

  Scenario: I cannot add a new user without his last name
    Given I have an User configuration without last_name
    When I do a POST request to the user endpoint
    Then I receive an error that the last_name is required

  Scenario: I cannot add a new user without his email
    Given I have an User configuration without email
    When I do a POST request to the user endpoint
    Then I receive an error that the email is required

  Scenario: I cannot add a new user with invalid email format
    Given I have an User configuration with invalid email format
    When I do a POST request to the user endpoint
    Then I receive an error that the email is invalid
