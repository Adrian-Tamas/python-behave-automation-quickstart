from pages.base_page import BasePage


class ReservationsPage(BasePage):

    table_row_locator = "//tr[@class='clickable-reservation-row']"
    reservations_btn = "//a[@id='v-pills-reservations']"
    edit_btn = "//button[@id='edit-reservation']"
    delete_btn = "//button[@id='delete-reservation']"
    create_btn = "//a[@id='create-reservation']"
    delete_title = "//h5[@id='deleteReservationModalTitle']"
    edit_title = "//h1[text()='Edit Reservation']"
    create_title = "//h1[text()='Create Reservation']"
    cancel_deleting = "//button[text()='Cancel']"
    cancel_edit = "//input[@value='Edit reservation']/following-sibling::*[1]"
    cancel_create = "//input[@value='Save reservation']/following-sibling::*[1]"
    reservations_title_locator = "//h1[text()='Reservations']"
    reservation_date_column_locator = "//th[text()='Reservation Date']"
    reservation_expiration_date_column_locator = "//th[text()='Reservation Expiration Date']"

    reservation_column_titles = [reservation_date_column_locator, reservation_expiration_date_column_locator]

    def __init__(self, driver):
        self.url = super().url + "/reservations"
        super().__init__(driver)

    def check_reservations_displayed(self):
        reservations = self.wait_presence_of_all_elements_located(self.table_row_locator)
        return len(reservations) > 0

    def click_on_create_btn(self):
        self.wait_element_to_be_clickable(self.create_btn).click()

    def click_on_edit_btn(self):
        self.wait_element_to_be_clickable(self.edit_btn).click()

    def click_on_delete_btn(self):
        self.wait_element_to_be_clickable(self.delete_btn).click()

    def click_on_reservations_btn(self):
        self.wait_element_to_be_clickable(self.reservations_btn).click()

    def click_on_first_reservations_row(self):
        reservations = self.wait_presence_of_all_elements_located(self.table_row_locator)
        reservations[0].click()

    def click_on_cancel_deleting(self):
        self.wait_element_to_be_clickable(self.cancel_deleting).click()

    def click_on_cancel_edit(self):
        self.wait_element_to_be_clickable(self.cancel_edit).click()

    def click_on_cancel_create(self):
        self.wait_element_to_be_clickable(self.cancel_create).click()

    def is_text_present_in_all_rows(self, text):
        reservations = self.wait_presence_of_all_elements_located(self.table_row_locator)
        for row in reservations:
            # print(f"********len: {len(row.text)}*******for {row.text}  ***********")
            if len(reservations[0].text) == 0 or len(row.text) != 0 and text not in row.text:
                return False
        return True

    def is_delete_message_displayed(self):
        delete_title = self.wait_presence_of_element_located(self.delete_title)
        if delete_title is not None:
            return True
        return False

    def is_edit_title_displayed(self):
        edit_title = self.wait_presence_of_element_located(self.edit_title)
        if edit_title is not None:
            return True
        return False

    def is_create_title_displayed(self):
        create_title = self.wait_presence_of_element_located(self.create_title)
        if create_title is not None:
            return True
        return False

    def is_button_enabled(self, button):
        if button == "edit_btn":
            btn = self.wait_presence_of_element_located(self.edit_btn)
        else:
            btn = self.wait_presence_of_element_located(self.delete_btn)
        if btn.is_enabled():
            return True
        return False

