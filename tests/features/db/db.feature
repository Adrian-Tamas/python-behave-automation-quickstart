@database
@ui

Feature: Check data is saved in the database

  @e2e
  Scenario: New books appear in the database
    Given I have a book config
    When I create a new book
    Then I can find the book in the database
    And I can see the book details in the ui
    And I can export the info into a file

    @db
  Scenario: New user appear in the database
    Given I have a user config
    When I create a new user
    Then I can find the user in the database