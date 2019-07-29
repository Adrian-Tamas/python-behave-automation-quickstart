from pages.base_page import BasePage


class CreateBookPage(BasePage):

    name_field_locator = "#name"
    author_field_locator = "#author"
    description_field_locator = "#description"
    cover_field_locator = "#cover"
    save_button_locator = "#save"

    def __init__(self, browser):
        super().__init__(browser)
        self.url = super().url + "/books/create"
        self.browser = browser

    def fill_in_book_details(self, book_details: dict):
        self.browser.find(self.name_field_locator, wait=True, ttl=self.max_timeout).write(book_details.get("name"))
        self.browser.find(self.author_field_locator, wait=True, ttl=self.max_timeout).write(book_details.get("author"))
        self.browser.find(self.description_field_locator, wait=True, ttl=self.max_timeout).write(book_details.get("description", ""))
        self.browser.find(self.cover_field_locator, wait=True, ttl=self.max_timeout).write(book_details.get("cover", ""))
        return self

    def click_save_book_button(self, next_page):
        self.browser.find(self.save_button_locator, wait=True, ttl=self.max_timeout).click()
        return next_page(self.browser)
