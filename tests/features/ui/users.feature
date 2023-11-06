@ui
@users_ui

Feature: Users Page

  Scenario: Get all Users
    Given I have at least 1 user
    When I navigate to the users page
    Then I can see a list of available users

  Scenario: I can add a one User
    Given I have details for a new user
    And I open the create users page
    When I enter the details and save the user details
    Then the user is saved

  Scenario: Filter user
    Given I have at least 1 user
    When I navigate to the users page
    And I search for a partial user match of 'Merrill'
    Then all the users displayed will have 'Merrill' in the name

  Scenario: View user details
    Given I have at least 1 user
    When I navigate to the users page
    And I open the user details
    Then all the expected user details are present