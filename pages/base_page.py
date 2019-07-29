from configuration.configuration import frontend_url, max_timeout
from abc import ABC


class BasePage(ABC):

    url = frontend_url
    books_button_identifier = "#v-pills-books"
    users_button_identifier = "#v-pills-users"
    reservations_button_identifier = "#v-pills-reservations"

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
