@backend
@book
@delete_book

Feature: Delete books

  Scenario: I can delete a book using a valid book_id
    Given I have a new book added into database
    And I have the related book id
    When I do a DELETE request to the book endpoint
    Then I deleted successfully the book from database

  Scenario: I cannot delete an user using an invalid user_id
    Given I have an user_id for an user that doesn't exist
    When I do a DELETE request to the user endpoint with that ID
    Then I receive an error that the user was not found