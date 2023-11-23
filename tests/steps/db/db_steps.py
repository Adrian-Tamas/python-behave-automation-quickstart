import csv
from time import sleep

from assertpy import assert_that
from behave import given, when, then

from database.database import SQLiteDatabaseConnection
from models.books_model import get_valid_with_all_params_create_book_payload
from models.users_model import get_valid_create_user_payload
from tests.steps.book.backend.create_book_steps import when_i_do_a_post_request_to_the_book_endpoint
from tests.steps.book.ui.books_steps import (when_i_navigate_to_the_books_page,
                                             when_i_open_the_book_details,
                                             then_all_the_expected_details_are_present)
from tests.steps.user.backend.create_user_steps import when_i_do_a_post_request_to_the_user_endpoint


@given(u'I have a book config')
def given_i_have_a_book_config(context):
    context.request_body = get_valid_with_all_params_create_book_payload()


@when(u'I create a new book')
def when_i_create_a_new_book(context):
    when_i_do_a_post_request_to_the_book_endpoint(context)


@then(u'I can find the book in the database')
def then_i_find_the_book_in_the_database(context):
    book_id = context.response.json()['id']
    db = SQLiteDatabaseConnection()
    with db:
        book = db.get_book_by_id(book_id)
        assert_that(book).is_not_none()
        book = book.serialize()
    assert_that(book).is_equal_to(context.response.json())


@given(u'I have a user config')
def given_i_have_a_user_config(context):
    context.request_body = get_valid_create_user_payload()


@when(u'I create a new user')
def when_i_create_a_new_user(context):
    when_i_do_a_post_request_to_the_user_endpoint(context)


@then(u'I can find the user in the database')
def then_i_can_find_the_user_in_the_database(context):
    user_id = context.response.json()['id']
    db = SQLiteDatabaseConnection()
    with db:
        user = db.get_user_by_id(user_id)
        assert_that(user).is_not_none()
        user = user.serialize()
    assert_that(user).is_equal_to(context.response.json())


@then(u'I can see the book details in the ui')
def the_i_can_see_the_book_details_in_the_ui(context):
    when_i_navigate_to_the_books_page(context)
    sleep(10)
    when_i_open_the_book_details(context)
    sleep(2)
    then_all_the_expected_details_are_present(context)


@then(u'I can export the info into a file')
def then_i_can_export_the_info_into_a_file(context):
    with open("book.csv", "w", newline='') as f:
        fieldnames = ['id', 'name', 'author', 'description', 'cover']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(context.response.json())