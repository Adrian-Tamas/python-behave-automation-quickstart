from assertpy import assert_that
from behave import given, when, then
from faker import Faker

from actions.api.book_endpoint_actions import do_put_request_to_update_book

fake = Faker()


# GIVENs
@given('I want to change the title and author')
def given_i_want_to_change_the_title_and_author(context):
    context.new_title = fake.text(20)
    context.new_author = fake.name()
    context.request_body['name'] = context.new_title
    context.request_body['author'] = context.new_author


# WHENs
@when('I do a PUT request to the book endpoint')
def when_i_do_a_put_request_to_the_book_endpoint(context):
    context.book_id = context.response.json()['id']
    context.response = do_put_request_to_update_book(book_id=context.book_id, data=context.request_body)


@when('I try to update book with the same details')
def when_i_try_to_update_book_with_the_same_details(context):
    when_i_do_a_put_request_to_the_book_endpoint(context)


# THENs
@then('the response is with success and the updated book details are displayed')
def then_the_response_is_with_success_and_the_updated_book_details_are_displayed(context):
    assert_that(context.response.status_code).is_equal_to(200)
    assert_that(context.response.json()).is_equal_to(context.request_body, ignore='id')
    assert_that(context.response.json()['id']).is_equal_to(context.book_id)
