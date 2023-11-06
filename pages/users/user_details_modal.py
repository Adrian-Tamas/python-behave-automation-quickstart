from configuration.configuration import max_timeout
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserDetailsModal:
    title = "User Details"
    modal_locator = "#viewUserDetailsModal"
    title_locator = "#itemLabel"
    cover_locator = "#preview"
    user_name_locator = "#user_name"
    user_email_locator = "#user_email"

    def __init__(self, driver):
        self.driver = driver
        self.max_timeout = max_timeout

    def check_modal_is_displayed(self):
        modal_element = WebDriverWait(self.driver, self.max_timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.modal_locator))
        )
        return modal_element.is_displayed()

    def check_modal_title(self):
        title_element = self.driver.find_element(By.CSS_SELECTOR, self.title_locator)
        return title_element.text == self.title

    def check_user_details(self, user):
        user_name_element = (self.driver.find_element(By.CSS_SELECTOR, self.user_name_locator)).text
        user_email_element = (self.driver.find_element(By.CSS_SELECTOR, self.user_email_locator)).text
        user_name_to_verify = user["first_name"] + " " + user["last_name"]
        user_email_to_verify = user["email"]
        details_are_present = (user_name_element == user_name_to_verify) and (user_email_element == user_email_to_verify)
        return details_are_present
