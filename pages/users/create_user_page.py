from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CreateUserPage(BasePage):

    first_name_field_locator = (By.CSS_SELECTOR, "#first_name")
    last_name_field_locator = (By.CSS_SELECTOR, "#last_name")
    email_field_locator = (By.CSS_SELECTOR, "#email")
    confirm_email_field_locator = (By.CSS_SELECTOR, "#confirm_email")
    save_button_locator = (By.CSS_SELECTOR, "#save")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = super().url + "/users/create"

    def fill_in_user_details(self, user_details: dict):
        first_name_field = self.wait_visibility_of_element_located(self.first_name_field_locator)
        last_name_field = self.wait_visibility_of_element_located(self.last_name_field_locator)
        email_field = self.wait_visibility_of_element_located(self.email_field_locator)
        confirm_email_field = self.wait_visibility_of_element_located(self.confirm_email_field_locator)
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
        self.wait_element_to_be_clickable(self.save_button_locator).click()
        return next_page(self.driver)


