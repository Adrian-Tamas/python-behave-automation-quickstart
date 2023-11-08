from pages.base_page import BasePage
from pages.users.user_details_modal import UserDetailsModal

class UsersPage(BasePage):
    table_row_locator = "//*[@class='clickable-row']"
    create_user_button_locator = "//*[contains(text(),'Create')]"
    user_first_name_column_locator = "//th[text()='User First Name']"
    user_last_name_column_locator = "//th[text()='User First Name']"
    user_email_column_locator = "//th[text()='User Email']"  # Common for users and reservations

    user_column_titles = [user_first_name_column_locator, user_last_name_column_locator, user_email_column_locator]

    def __init__(self, driver):
        super().__init__(driver)
        self.url = super().url + "/users"

    def check_users_displayed(self):
        users = self.wait_presence_of_element_located(self.table_row_locator)
        return len(users) > 0

    def open_create_users(self, next_page):
        self.wait_element_to_be_clickable(self.create_user_button_locator).click()
        return next_page(self.driver)

    def is_success_message_displayed(self, user_name):
        success_msg = self.wait_presence_of_element_located(self.save_success_message_locator)
        check_message = f"User with name {user_name} was created successfully" in success_msg.text
        return check_message

    def is_user_present_on_page(self, user):
        users = self.wait_presence_of_element_located(self.table_row_locator)
        for row in users:
            row_text = row.text
            if user.get("first_name") in row_text and user.get("email") in row_text:
                return True
        return False

    def is_text_present_in_all_rows(self, text):
        users = self.wait_presence_of_element_located(self.table_row_locator)
        for row in users:
            if row.text != "" and text not in row.text:
                return False
        return True

    def open_user_details(self, user_id):
        self.select_table_row(data_id=user_id)
        self.wait_element_to_be_clickable(self.view_details_button_locator).click()
        return UserDetailsModal(self.driver)
