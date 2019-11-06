from time import sleep

from assertpy import assert_that
from behave import given, when, then
from pages.books.books_page import BooksPage
from faker import Faker

from pages.books.create_book_page import CreateBookPage

fake = Faker()


@given(u'I have at least 1 book')
def given_i_have_at_least_one_book(context):
    pass  # TODO: use api to insert a book


@when(u'I navigate to the books page')
def when_i_navigate_to_the_books_page(context):
    context.browser.navigate(BooksPage.url)
    context.books_page = BooksPage(context.browser)


@then(u'I can see a list of available books')
def then_i_can_see_a_list_of_available_books(context):
    assert_that(context.books_page.check_books_displayed()).is_true()


@given(u'I have details for a new book')
def given_i_have_details_for_a_new_book(context):
    context.book = {
        "name": fake.text(20),
        "author": fake.name()
    }


@given(u'I open the Add books page')
def given_i_open_the_add_books_page(context):
    books_page = BooksPage(context.browser)
    context.browser.navigate(books_page.url)
    context.create_book_page = books_page.open_create_book(CreateBookPage)


@when(u'I enter the details and save the book')
def when_i_enter_the_details_and_save_the_book(context):
    context.books_page = context\
        .create_book_page.fill_in_book_details(context.book)\
        .click_save_book_button(BooksPage)


@then(u'the book is saved')
def then_the_book_is_saved(context):
    assert_that(context.books_page.is_success_message_displayed(context.book.get("name"))).is_true()
    assert_that(context.books_page.is_book_present_on_page(context.book)).is_true()
