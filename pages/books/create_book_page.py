from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CreateBookPage(BasePage):

    name_field_locator = (By.CSS_SELECTOR, "#name")
    author_field_locator = (By.CSS_SELECTOR, "#author")
    description_field_locator = (By.CSS_SELECTOR, "#description")
    cover_field_locator = (By.CSS_SELECTOR, "#cover")
    save_button_locator = (By.CSS_SELECTOR, "#save")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = super().url + "/books/create"

    def fill_in_book_details(self, book_details: dict):

        name_field = self.wait_presence_of_element_located(self.name_field_locator)
        author_field = self.wait_presence_of_element_located(self.author_field_locator)
        description_field = self.wait_presence_of_element_located(self.description_field_locator)
        cover_field = self.wait_presence_of_element_located(self.cover_field_locator)

        name_field.clear()
        name_field.send_keys(book_details.get("name"))
        author_field.clear()
        author_field.send_keys(book_details.get("author"))
        description_field.clear()
        description_field.send_keys(book_details.get("description", ""))
        cover_field.clear()
        cover_field.send_keys(book_details.get("cover", ""))
        return self

    def click_save_book_button(self, next_page):
        self.wait_element_to_be_clickable(self.save_button_locator).click()
        return next_page(self.driver)

