from configuration.configuration import max_timeout


class BookDetailsModal:

    title = "Book Details"
    modal_locator = "#viewBookDetails"
    title_locator = "#itemLabel"
    cover_locator = "#preview"
    book_name_locator = "#book_name"
    author_name_locator = "#book_author"
    book_description_locator = "#book_description"

    def __init__(self, browser):
        self.browser = browser
        self.max_timeout = max_timeout

    def check_modal_is_displayed(self):
        return self.browser.find(self.modal_locator, wait=True, ttl=self.max_timeout).is_displayed()

    def check_modal_title(self):
        return self.browser.find(self.title_locator, wait=True, ttl=self.max_timeout).text() == self.title

    def check_book_details(self, book):
        return (self.browser.find(self.cover_locator, wait=True, ttl=self.max_timeout).attribute("src") == book["cover"]
                and self.browser.find(self.book_name_locator, wait=True, ttl=self.max_timeout).text() == book["name"]
                and self.browser.find(self.author_name_locator, wait=True, ttl=self.max_timeout).text() == book["author"]
                and self.browser.find(self.book_description_locator, wait=True, ttl=self.max_timeout).text() == book["description"])
