from configuration.configuration import max_timeout
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookDetailsModal:

    title = "Book Details"
    modal_locator = "#viewBookDetails"
    title_locator = "#itemLabel"
    cover_locator = "#preview"
    book_name_locator = "#book_name"
    author_name_locator = "#book_author"
    book_description_locator = "#book_description"

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

    def check_book_details(self, book):
        cover_element = self.driver.find_element(By.CSS_SELECTOR, self.cover_locator)
        book_name_element = self.driver.find_element(By.CSS_SELECTOR, self.book_name_locator)
        author_name_element = self.driver.find_element(By.CSS_SELECTOR, self.author_name_locator)
        book_description_element = self.driver.find_element(By.CSS_SELECTOR, self.book_description_locator)

        return (cover_element.get_attribute("src") == book["cover"]
                and book_name_element.text == book["name"]
                and author_name_element.text == book["author"]
                and book_description_element.text == book["description"])
