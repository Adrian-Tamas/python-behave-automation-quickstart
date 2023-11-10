from pages.base_page import BasePage
from pages.books.book_details_modal import BookDetailsModal


class BooksPage(BasePage):

    table_row_locator = "//tr[@class='clickable-row']"
    create_book_button_locator = "//a[@id='create']"

    def __init__(self, driver):
        super().__init__(driver)
        self.url = super().url + "/books"

    def check_books_displayed(self):
        books = self.wait_presence_of_all_elements_located(self.table_row_locator)
        return len(books) > 0

    def open_create_book(self, next_page):
        self.wait_element_to_be_clickable(self.create_book_button_locator).click()
        return next_page(self.driver)

    def is_success_message_displayed(self, book_name):
        success_msg = self.wait_presence_of_element_located(self.save_success_message_locator)
        check_message = f"Book '{book_name}' was successfully saved" in success_msg.text
        return check_message

    def is_book_present_on_page(self, book):
        books = self.wait_presence_of_all_elements_located(self.table_row_locator)
        for row in books:
            row_text = row.text
            if book.get("name") in row_text and book.get("author") in row_text:
                return True
        return False

    def is_text_present_in_all_rows(self, text):
        books = self.wait_presence_of_all_elements_located(self.table_row_locator)

        for row in books:
            if row.text != "" and text not in row.text:
                return False
        return True

    def open_book_details(self, book_id):
        self.select_table_row(data_id=book_id)
        self.wait_element_to_be_clickable(self.view_details_button_locator).click()
        return BookDetailsModal(self.driver)