@backend
@book
@get_books

Feature: View all books and by book id

  Scenario: I can view all books
    Given I already have at least one book
    When I do a get all books request
    Then I should receive a 200 response code and a book has the correct attributes

  Scenario: I get the list of books incremented after each new book added
    Given I get the number of existing books
    And I already have a book
    When I get the number of books
    Then in the end the list of books is larger with one item

  Scenario: I get the book details when I make a request with correct book id
    Given I already have a book
    When I do a get request for one book with correct book_id
    Then the related book payload is successfully displayed

  Scenario: I get an error when I make a request for book details with a not existing book id
    Given I have a book_id for a book that doesn't exist
    When I do a get request for one book with that book_id
    Then I receive an error that the book was not found
