from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CreateUserPage(BasePage):

    first_name_field_locator = "#first_name"
    last_name_field_locator = "#last_name"
    email_field_locator = "#email"
    confirm_email_field_locator = "#confirm_email"
    save_button_locator = "#save"

    def __init__(self, driver):
        super().__init__(driver)
        self.url = super().url + "/users/create"

    def fill_in_user_details(self, user_details: dict):
        first_name_field = self.driver.find_element(By.CSS_SELECTOR, self.first_name_field_locator)
        last_name_field = self.driver.find_element(By.CSS_SELECTOR, self.last_name_field_locator)
        email_field = self.driver.find_element(By.CSS_SELECTOR, self.email_field_locator)
        confirm_email_field = self.driver.find_element(By.CSS_SELECTOR, self.confirm_email_field_locator)
        first_name_field.clear()
        first_name_field.send_keys(user_details.get("first_name"))
        last_name_field.clear()
        last_name_field.send_keys(user_details.get("last_name"))
        email_field.clear()
        email_field.send_keys(user_details.get("email"))
        confirm_email_field.clear()
        confirm_email_field.send_keys(user_details.get("email"))
        return self

    def click_save_user_button(self, next_page):
        save_button = self.driver.find_element(By.CSS_SELECTOR, self.save_button_locator)
        save_button.click()
        return next_page(self.driver)


