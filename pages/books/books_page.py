from pages.base_page import BasePage
from pages.books.book_details_modal import BookDetailsModal


class BooksPage(BasePage):

    table_row_locator = ".clickable-row"
    create_book_button_locator = "#create"
    view_details_button_locator = "#viewDetails"
    save_success_message_locator = ".alert-success"

    def __init__(self, browser):
        super().__init__(browser)
        self.url = super().url + "/books"
        self.browser = browser

    def check_books_displayed(self):
        books = self.browser.find(self.table_row_locator)
        return len(books) > 0

    def open_create_book(self, next_page):
        self.browser.find(self.create_book_button_locator, wait=True, ttl=self.max_timeout).click()
        return next_page(self.browser)

    def is_success_message_displayed(self, book_name):
        success_msg = self.browser.find(self.save_success_message_locator, wait=True, ttl=self.max_timeout)
        check_message = f"Book '{book_name}' was successfully saved" in success_msg.text()
        return len(success_msg) == 1 and check_message

    def is_book_present_on_page(self, book):
        books = self.browser.find(self.table_row_locator)
        for row in books:
            row_text = row.text()
            if book.get("name") in row_text and book.get("author") in row_text:
                return True
        return False

    def is_text_present_in_all_rows(self, text):
        books = self.browser.find(self.table_row_locator)
        for row in books:
            if text not in row.text():
                return False
        return True

    def open_book_details(self, book_id):
        self.select_table_row(data_id=book_id)
        self.browser.find(self.view_details_button_locator, wait=True, ttl=self.max_timeout).click()
        return BookDetailsModal(self.browser)
