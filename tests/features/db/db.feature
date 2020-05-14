@db

Feature: Check data is saved in the database

  Scenario: New books appear in the database
    Given I have a book config
    When I create a new book
    Then I can find the book in the database

  Scenario: New user appear in the database
    Given I have a user config
    When I create a new user
    Then I can find the user in the database