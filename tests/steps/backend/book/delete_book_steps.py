from assertpy import assert_that
from behave import given, when, then

from actions.api.book_endpoint_actions import do_delete_request_for_book


# GIVENs
@given('I have the related book id')
def given_i_have_the_related_book_id(context):
    context.book_id = context.response.json()['id']


# WHENs
@when('I do a DELETE request to the book endpoint')
def when_i_do_a_delete_request_to_the_book_endpoint(context):
    context.response = do_delete_request_for_book(context.book_id)


@when('I do a DELETE request to the book endpoint with that ID')
def when_i_do_a_delete_request_to_the_book_endpoint_with_that_id(context):
    context.response = do_delete_request_for_book(context.not_existing_book_id)


# THENs
@then('I deleted successfully the book from database')
def then_i_deleted_successfully_the_book_from_database(context):
    assert_that(context.response.status_code).is_equal_to(200)
    assert_that(context.response.json()).is_equal_to(f'Book with id {context.book_id} has been deleted')
