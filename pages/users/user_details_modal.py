from configuration.configuration import max_timeout
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class UserDetailsModal(BasePage):

    title = "User Details"
    modal_locator = (By.CSS_SELECTOR, "#viewUserDetailsModal")
    title_locator = (By.CSS_SELECTOR, "#itemLabel")
    cover_locator = (By.CSS_SELECTOR, "#preview")
    user_name_locator = (By.CSS_SELECTOR, "#user_name")
    user_email_locator = (By.CSS_SELECTOR, "#user_email")

    def __init__(self, driver):
        super().__init__(driver)
        self.max_timeout = max_timeout

    def check_modal_is_displayed(self):
        modal_element = self.wait_visibility_of_element_located(self.modal_locator)
        return modal_element.is_displayed()

    def check_modal_title(self):
        title_element = self.wait_presence_of_element_located(self.title_locator)
        return title_element.text == self.title

    def check_user_details(self, user):
        user_name_element = (self.wait_visibility_of_element_located(self.user_name_locator)).text
        user_email_element = (self.wait_visibility_of_element_located(self.user_email_locator)).text
        user_name_to_verify = user["first_name"] + " " + user["last_name"]
        user_email_to_verify = user["email"]
        details_are_present = (user_name_element == user_name_to_verify) and (user_email_element == user_email_to_verify)
        return details_are_present
