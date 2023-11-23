from configuration.configuration import max_timeout
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BookDetailsModal(BasePage):

    title = "Book Details"
    modal_locator = (By.CSS_SELECTOR, "#viewBookDetails")
    title_locator = (By.CSS_SELECTOR, "#itemLabel")
    cover_locator = (By.CSS_SELECTOR, "#preview")
    book_name_locator = (By.CSS_SELECTOR, "#book_name")
    author_name_locator = (By.CSS_SELECTOR, "#book_author")
    book_description_locator = (By.CSS_SELECTOR, "#book_description")

    def __init__(self, driver):
        super().__init__(driver)
        self.max_timeout = max_timeout

    def check_modal_is_displayed(self):
        modal_element = self.wait_visibility_of_element_located(self.modal_locator)
        return modal_element.is_displayed()

    def check_modal_title(self):
        title_element = self.wait_visibility_of_element_located(self.title_locator)
        return title_element.text == self.title

    def check_book_details(self, book):
        cover_element = self.wait_visibility_of_element_located(self.cover_locator)
        book_name_element = self.wait_visibility_of_element_located(self.book_name_locator)
        author_name_element = self.wait_visibility_of_element_located(self.author_name_locator)
        book_description_element = self.wait_visibility_of_element_located(self.book_description_locator)

        return (cover_element.get_attribute("src") == book["cover"]
                and book_name_element.text == book["name"]
                and author_name_element.text == book["author"]
                and book_description_element.text == book["description"])
