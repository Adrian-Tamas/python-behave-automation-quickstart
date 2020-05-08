@backend
@book
@delete_book

Feature: Delete books

  Scenario: I can delete a book using a valid book_id
    Given I already have a book added only with the required parameters
    And I have the related book id
    When I do a DELETE request to the book endpoint
    Then I deleted successfully the book from books list

  Scenario: I cannot delete a user using an invalid user_id
    Given I have an user_id for an user that doesn't exist
    When I do a DELETE request to the user endpoint with that ID
    Then I receive an error that the user was not found
