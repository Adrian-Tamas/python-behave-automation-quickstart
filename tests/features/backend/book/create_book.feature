@backend
@book
@create_book

Feature: Create books

  Scenario: I can add a new book to the database
    Given I have a correct Book configuration
    When I do a POST request to the book endpoint
    Then the request will be successful with 200 response code
    And the response will contain the new object with the related ID

  Scenario: I cannot add several books with the same name and author
    Given I have a new book added into database
    When I try to add another book with the same details
    Then I receive an error that the book with that name already exists

  Scenario: I cannot add a new book without his title
    Given I have a Book configuration without name
    When I do a POST request to the book endpoint
    Then I receive an error that the name is required

  Scenario: I cannot add a new book without his author
    Given I have a Book configuration without author
    When I do a POST request to the book endpoint
    Then I receive an error that the author is required
