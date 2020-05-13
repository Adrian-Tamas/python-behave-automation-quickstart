@ui

Feature: Books Page

  Scenario: Get all Books
    Given I have at least 1 book
    When I navigate to the books page
    Then I can see a list of available books

  Scenario: I can add a Book
    Given I have details for a new book
    And I open the Add books page
    When I enter the details and save the book
    Then the book is saved

  Scenario: Filter books
    Given I have at least 1 book
    When I navigate to the books page
    And I search for a partial title match of 'Angel'
    Then all the books displayed will have 'Angel' in the name

  Scenario: View book details
    Given I have at least 1 book
    When I navigate to the books page
    And I open the book details
    Then all the expected details are present