import uuid

from assertpy import assert_that
from behave import given, when, then

from actions.api.book_endpoint_actions import do_get_request_for_all_books, do_get_request_for_book
from tests.steps.book.backend.create_book_steps import (
    given_i_have_a_correct_book_payload_only_with_the_required_parameters,
    when_i_do_a_post_request_to_the_book_endpoint)


# GIVENs
@given('I already have at least one book')
def given_i_already_have_at_least_one_book(context):
    given_i_have_a_correct_book_payload_only_with_the_required_parameters(context)
    when_i_do_a_post_request_to_the_book_endpoint(context)


@given('I get the number of existing books')
def given_i_get_the_number_of_existing_books(context):
    all_books_response = do_get_request_for_all_books()
    context.number_of_books_before = len(all_books_response.json())


@given("I have a book_id for a book that doesn't exist")
def given_i_have_a_book_id_for_a_book_that_does_not_exist(context):
    context.not_existing_book_id = str(uuid.uuid4())


# WHENs
@when('I do a get all books request')
def when_i_do_a_get_all_books_request(context):
    context.all_books_response = do_get_request_for_all_books()


@when('I get the number of books')
def when_i_get_the_number_of_books(context):
    all_books_response = do_get_request_for_all_books()
    context.number_of_books_after = len(all_books_response.json())


@when('I do a get request for one book with correct book_id')
def when_i_do_a_get_request_for_one_book_with_correct_book_id(context):
    context.valid_book_id = context.response.json()['id']
    context.response = do_get_request_for_book(book_id=context.valid_book_id)


@when('I do a get request for one book with that book_id')
def when_i_do_a_get_request_for_one_book_with_that_book_id(context):
    context.response = do_get_request_for_book(book_id=context.not_existing_book_id)


# THENs
@then('I should receive a 200 response code and a book has the correct attributes')
def then_i_should_receive_a_200_response_code_and_a_book_has_the_correct_attributes(context):
    assert_that(context.all_books_response.status_code).is_equal_to(200)
    assert_that(context.all_books_response.json()[0]).contains('id', 'name', 'author')


@then('in the end the list of books is larger with one item')
def then_in_the_end_the_list_of_books_is_larger_with_one_item(context):
    assert_that(context.number_of_books_after).is_equal_to(context.number_of_books_before + 1)


@then('the related book payload is successfully displayed')
def then_the_related_book_payload_is_successfully_displayed(context):
    book = context.response.json()
    assert_that(context.response.status_code).is_equal_to(200)
    assert_that(book['id']).is_equal_to(context.valid_book_id)
    assert_that(book).is_equal_to(context.request_body, ignore=['id', 'description', 'cover'])


@then('I receive an error that the book was not found')
def then_i_receive_an_error_that_the_book_was_not_found(context):
    assert_that(context.response.status_code).is_equal_to(400)
    assert_that(context.response.json()).is_equal_to(f'Book with id = {context.not_existing_book_id} was not found')
