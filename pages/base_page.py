from configuration.configuration import frontend_url, max_timeout
from abc import ABC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import TimeoutException


class BasePage(ABC):
    url = frontend_url
    books_button_identifier = "#v-pills-books"
    users_button_identifier = "#v-pills-users"
    reservations_button_identifier = "#v-pills-reservations"
    search_field_identifier = "//input[@id='searchField']"
    row_selector = "//tr[@class='clickable-row'][@data-id='{0}']"

    def __init__(self, driver):
        self.driver = driver
        self.max_timeout = max_timeout

    def go_to_books_page(self, next_page):
        self.wait_element_to_be_clickable(self.books_button_identifier).click()
        return next_page(self.driver)

    def go_to_users_page(self, next_page):
        self.wait_element_to_be_clickable(self.users_button_identifier).click()
        return next_page(self.driver)

    def go_to_reservations_page(self, next_page):
        self.wait_element_to_be_clickable(self.reservations_button_identifier).click()
        return next_page(self.driver)

    def filter_table(self, search_term):
        input_element = self.wait_presence_of_element_located(self.search_field_identifier)
        input_element.clear()
        input_element.send_keys(search_term)
        return self

    def select_table_row(self, data_id):
        self.wait_element_to_be_clickable(self.row_selector.format(data_id)).click()

    def wait_presence_of_element_located(self, element, timeout=max_timeout):
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, element)))
            return el
        except TimeoutException:
            print("TimeoutException: Elements are not located")

    def wait_presence_of_all_elements_located(self, element, timeout=max_timeout):
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, element)))
            return el
        except TimeoutException:
            print("TimeoutException: Elements are not located")

    def wait_element_to_be_clickable(self, element, timeout=max_timeout):
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, element)))
            return el
        except TimeoutException:
            print("TimeoutException: Element is not clickable")

    def wait_visibility_of_element_located(self, element, timeout=max_timeout):
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, element)))
            return el
        except TimeoutException:
            print("TimeoutException: Element is not visible")

