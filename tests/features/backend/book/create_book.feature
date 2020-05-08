@backend
@book
@create_book

Feature: Create books

  Scenario: I can add a new book only with the required parameters
    Given I have a correct book payload only with the required parameters
    When I do a POST request to the book endpoint
    Then the request will be successful with 200 response code
    And the response will contain the new book with the related ID

  Scenario: I can add a new book providing all the parameters
    Given I have a correct book payload with all the parameters
    When I do a POST request to the book endpoint
    Then the request will be successful with 200 response code
    And the response will contain the new object with the related ID
@fail
  Scenario: I can add a new book using existing author, but different title
    Given I have a correct book payload only with the required parameters
    And I do a POST request to the book endpoint
    When I add a new book using the same author as before
    Then the request will be successful with 200 response code
    And the response will contain the new book with the related ID

  Scenario: I can add a new book using existing title, but different author
    Given I already have a book added only with the required parameters
    And I do a POST request to the book endpoint
    When I add a new book using the same name as before
    Then the request will be successful with 200 response code
    And the response will contain the new book with the related ID

  Scenario: I cannot add several books with the same name and author
    Given I already have a book added only with the required parameters
    When I try to add another book with the same details
    Then I receive an error that the book with that name already exists

  Scenario: I cannot add a new book without its title
    Given I have a Book payload without name
    When I do a POST request to the book endpoint
    Then I receive an error that the name is required

  Scenario: I cannot add a new book without its author
    Given I have a Book payload without author
    When I do a POST request to the book endpoint
    Then I receive an error that the author is required
