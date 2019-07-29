from pages.base_page import BasePage


class ReservationsPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.url = super().url + "/reservations"
        self.browser = browser
