from configuration.configuration import frontend_url, max_timeout
from abc import ABC


class BasePage(ABC):

    url = frontend_url
    books_button_identifier = "#v-pills-books"
    users_button_identifier = "#v-pills-users"
    reservations_button_identifier = "#v-pills-reservations"
    search_field_identifier = "#searchField"
    row_selector = ".clickable-row[data-id='{0}']"

    def __init__(self, browser):
        self.browser = browser
        self.max_timeout = max_timeout

    def go_to_books_page(self, next_page):
        self.browser.find(self.books_button_identifier, wait=True, ttl=self.max_timeout).click()
        return next_page(self.browser)

    def go_to_users_page(self, next_page):
        self.browser.find(self.users_button_identifier, wait=True, ttl=self.max_timeout).click()
        return next_page(self.browser)

    def go_to_reservations_page(self, next_page):
        self.browser.find(self.reservations_button_identifier, wait=True, ttl=self.max_timeout).click()
        return next_page(self.browser)

    def filter_table(self, search_term):
        self.browser.find(self.search_field_identifier, wait=True, ttl=self.max_timeout).write(search_term)
        return self

    def select_table_row(self, data_id):
        self.browser.find(self.row_selector.format(data_id), wait=True, ttl=self.max_timeout).click()
