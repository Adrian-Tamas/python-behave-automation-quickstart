@ui

Feature: Books Page

  Scenario: Get all Books
    Given I have at least 1 book
    When I navigate to the books page
    Then I can see a list of available books

  @test
  Scenario: I can add a Book
    Given I have details for a new book
    And I open the Add books page
    When I enter the details and save the book
    Then the book is saved