from assertpy import assert_that
from behave import given, when, then
from pages.books.books_page import BooksPage
from faker import Faker

from pages.books.create_book_page import CreateBookPage
from tests.steps.book.backend.create_book_steps import (given_i_have_a_correct_book_payload_with_all_the_parameters,
                                                        when_i_do_a_post_request_to_the_book_endpoint)

fake = Faker()

@given(u'I have at least 1 book')
def given_i_have_at_least_one_book(context):
    given_i_have_a_correct_book_payload_with_all_the_parameters(context)
    when_i_do_a_post_request_to_the_book_endpoint(context)

@when(u'I navigate to the books page')
def when_i_navigate_to_the_books_page(context):
    context.driver.get(BooksPage.url)
    context.books_page = BooksPage(context.driver)

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
    books_page = BooksPage(context.driver)
    context.driver.get(books_page.url)
    context.create_book_page = books_page.open_create_book(CreateBookPage)

@when(u'I enter the details and save the book')
def when_i_enter_the_details_and_save_the_book(context):
    context.books_page = context.create_book_page.fill_in_book_details(context.book).click_save_book_button(BooksPage)

@when(u"I search for a partial title match of '{search_term}'")
def when_i_search_for_a_partial_title_match(context, search_term):
    context.books_page.filter_table(search_term)

@when(u'I open the book details')
def when_i_open_the_book_details(context):
    book_id = context.response.json()['id']
    context.details_modal = context.books_page.open_book_details(book_id)

@then(u'all the expected details are present')
def then_all_the_expected_details_are_present(context):
    book = context.response.json()
    book_details_modal = context.details_modal
    assert_that(book_details_modal.check_modal_is_displayed()).is_true()
    assert_that(book_details_modal.check_modal_title()).is_true()
    assert_that(book_details_modal.check_book_details(book)).is_true()


@then(u"all the books displayed will have '{search_term}' in the name")
def then_books_are_filtered(context, search_term):
    assert_that(context.books_page.is_text_present_in_all_rows(search_term)).is_true()


@then(u'the book is saved')
def then_the_book_is_saved(context):
    assert_that(context.books_page.is_success_message_displayed(context.book.get("name"))).is_true()
    assert_that(context.books_page.is_book_present_on_page(context.book)).is_true()


