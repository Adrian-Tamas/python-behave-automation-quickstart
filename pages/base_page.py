import logging
from configuration.configuration import frontend_url, max_timeout
from abc import ABC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.common.by import By
from icecream import ic


class BasePage(ABC):
    logging.basicConfig(filename='info.log', encoding='utf-8', level=logging.INFO)
    url = frontend_url
    books_button_identifier = (By.CSS_SELECTOR, "#v-pills-books")
    users_button_identifier = (By.CSS_SELECTOR, "#v-pills-users")
    reservations_button_identifier = (By.CSS_SELECTOR, "#v-pills-reservations")
    search_field_identifier = (By.CSS_SELECTOR, "#searchField")
    row_selector = (By.CSS_SELECTOR, ".clickable-row[data-id='{0}']")
    view_details_button_locator = (By.XPATH, "//*[contains(text(),'View Details')]")
    save_success_message_locator = (By.XPATH, "//*[@class='alert alert-success']")
    hash_character_locator = (By.XPATH, "//th[text()='#']")

    def __init__(self, driver):
        self.driver = driver
        self.max_timeout = max_timeout

    def is_page_title_displayed(self, page_title_locator):
        current_page_title = page_title_locator.split('=')[-1][:-1].strip()
        logging.info(f" Method called from: {ic.format().strip(' ic|')}\nIs {current_page_title} page title visible?")
        page_title = self.wait_presence_of_element_located(page_title_locator)

        if page_title:
            logging.info(f" Title {current_page_title} is visible")
            return True
        else:
            logging.info(f" Title {current_page_title} is NOT visible")
            return False

    def is_tab_displayed(self, tab_locator):
        current_tab = tab_locator.split('-')[-1][:-2].strip().capitalize()
        logging.info(f" Method called from: {ic.format().strip(' ic|')}\nIs '{current_tab}' tab visible?")
        tab = self.wait_presence_of_element_located(tab_locator)

        if tab:
            logging.info(f" Tab '{current_tab}' is visible")
            return True
        else:
            logging.info(f" Tab '{current_tab}' is NOT visible")
            return False

    def is_button_displayed(self, button_locator):
        current_button = button_locator.split(',')[-1][:-2].strip()
        logging.info(f" Method called from: {ic.format().strip(' ic|')}\nIs {current_button} button visible?")
        button = self.wait_presence_of_element_located(button_locator)

        if button:
            logging.info(f" Button {current_button} is visible")
            return True
        else:
            logging.info(f" Button {current_button} is NOT visible")
            return False

    def is_column_title_displayed(self, column_title_locator):
        current_column_title = column_title_locator.split('=')[-1][:-1].strip()
        logging.info(f" Method called from: {ic.format().strip(' ic|')}\nIs {current_column_title} column title visible?")
        column = self.wait_presence_of_element_located(column_title_locator)

        if column:
            logging.info(f" Column {current_column_title} is visible")
            return True
        else:
            logging.info(f" Column {current_column_title} is visible")
            return False

    # ACTIONS

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
        self.wait_element_to_be_clickable((self.row_selector[0], self.row_selector[1].format(data_id))).click()

    def wait_presence_of_element_located(self, by_locator, timeout=max_timeout):
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(by_locator))
            return el
        except TimeoutException:
            logging.info("TimeoutException: Elements are not located")

    def wait_presence_of_all_elements_located(self, by_locator, timeout=max_timeout):
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(by_locator))
            return el
        except TimeoutException:
            logging.info("TimeoutException: Elements are not located")

    def wait_element_to_be_clickable(self, by_locator, timeout=max_timeout):
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(by_locator))
            return el
        except TimeoutException:
            logging.info("TimeoutException: Element is not clickable")

    def wait_visibility_of_element_located(self, by_locator, timeout=max_timeout):
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(by_locator))
            return el
        except TimeoutException:
            logging.log("TimeoutException: Element is not visible")

