@backend
@book
@edit_book

Feature: Edit book details

  Scenario: I can successfully change the details of a book
    Given I have a new book added into database
    And I want to change the title and author
    When I do a PUT request to the book endpoint
    Then the response is with success and the updated book details are displayed

  Scenario: I get an error when I try to update book with the same details
    Given I have a new book added into database
    When I try to update book with the same details
    Then I receive an error that the book with that name already exists
