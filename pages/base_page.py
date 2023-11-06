import logging

from configuration.configuration import frontend_url, max_timeout
from abc import ABC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from icecream import ic


class BasePage(ABC):
    logging.basicConfig(filename='info.log', encoding='utf-8', level=logging.INFO)
    url = frontend_url
    # books_button_identifier = "#v-pills-books"
    # users_button_identifier = "#v-pills-users"
    # reservations_button_identifier = "#v-pills-reservations"
    # search_field_identifier = "#searchField"
    row_locator = "//*[@id='{0}']/th"

    # Tab locators
    books_tab_locator = "//*[@id='v-pills-books']"
    users_tab_locator = "//*[@id='v-pills-users']"
    reservations_tab_locator = "//*[@id='v-pills-reservations']"

    # Button locators
    view_details_button_locator = "//*[contains(text(),'View Details')]"
    create_button_locator = "//*[contains(text(),'Create')]"
    edit_button_locator = "//*[contains(text(),'Edit')]"
    delete_button_locator = "//*[contains(text(),'Delete')]"

    save_success_message_locator = "//*[@class='alert alert-success']"
    search_field_locator = "//*[@id='searchField']"
    hash_character_locator = "//th[text()='#']"

    def __init__(self, driver):
        self.driver = driver
        self.max_timeout = max_timeout

    # ELEMENT PRESENCE

    tab_elements = (books_tab_locator, users_tab_locator, reservations_tab_locator)
    button_elements = (view_details_button_locator, create_button_locator, edit_button_locator, delete_button_locator)

    def is_element_visible(self, locator, locator_type="XPATH"):
        if locator_type == "XPATH":
            locator_type = By.XPATH

        elif locator_type == "CSS":
            locator_type = By.CSS_SELECTOR
        element = WebDriverWait(self.driver, self.max_timeout).until(EC.visibility_of_element_located
                                                                     ((locator_type, locator)))
        return element

    def is_page_title_displayed(self, page_title_locator):
        current_page_title = page_title_locator.split('=')[-1][:-1].strip()
        logging.info(f" Method called from: {ic.format().strip(' ic|')}\nIs {current_page_title} page title visible?")
        page_title = self.is_element_visible(page_title_locator)

        if page_title:
            logging.info(f" Title {current_page_title} is visible")
            return True
        else:
            logging.info(f" Title {current_page_title} is NOT visible")
            return False

    def is_tab_displayed(self, tab_locator):
        current_tab = tab_locator.split('-')[-1][:-2].strip().capitalize()
        logging.info(f" Method called from: {ic.format().strip(' ic|')}\nIs '{current_tab}' tab visible?")
        tab = self.is_element_visible(tab_locator)

        if tab:
            logging.info(f" Tab '{current_tab}' is visible")
            return True
        else:
            logging.info(f" Tab '{current_tab}' is NOT visible")
            return False

    def is_button_displayed(self, button_locator):
        current_button = button_locator.split(',')[-1][:-2].strip()
        logging.info(f" Method called from: {ic.format().strip(' ic|')}\nIs {current_button} button visible?")
        button = self.is_element_visible(button_locator)

        if button:
            logging.info(f" Button {current_button} is visible")
            return True
        else:
            logging.info(f" Button {current_button} is NOT visible")
            return False

    def is_column_title_displayed(self, column_title_locator):
        current_column_title = column_title_locator.split('=')[-1][:-1].strip()
        logging.info(f" Method called from: {ic.format().strip(' ic|')}\nIs {current_column_title} column title visible?")
        column = self.is_element_visible(column_title_locator)

        if column:
            logging.info(f" Column {current_column_title} is visible")
            return True
        else:
            logging.info(f" Column {current_column_title} is visible")
            return False

    # ACTIONS

    def go_to_books_page(self, next_page):
        self.driver.find_element(By.XPATH, self.books_tab_locator).click()
        return next_page(self.driver)

    def go_to_users_page(self, next_page):
        self.driver.find_element(By.XPATH, self.users_tab_locator).click()
        return next_page(self.driver)

    def go_to_reservations_page(self, next_page):
        self.driver.find_element(By.XPATH, self.reservations_tab_locator).click()
        return next_page(self.driver)

    def filter_table(self, search_term):
        input_element = self.driver.find_element(By.XPATH, self.search_field_locator)
        input_element.clear()
        input_element.send_keys(search_term)
        return self

    def select_table_row(self, data_id):
        self.driver.find_element(By.XPATH, self.row_locator.format(data_id)).click()