from assertpy import assert_that
from behave import given, when, then

from actions.api.book_endpoint_actions import do_post_request_to_create_book
from models.books_model import get_valid_create_book_payload, get_add_book_payload_without_parameter


# GIVENs
@given('I have a correct book payload')
def given_i_have_a_correct_book_payload(context):
    context.request_body = get_valid_create_book_payload()


@given('I already have a book')
def given_i_already_have_a_book(context):
    given_i_have_a_correct_book_payload(context)
    when_i_do_a_post_request_to_the_book_endpoint(context)


@given('I have a Book payload without {entity_name}')
def given_i_have_a_book_payload_without_title(context, entity_name):
    context.request_body = get_add_book_payload_without_parameter(entity=entity_name)


# WHENs
@when('I do a POST request to the book endpoint')
def when_i_do_a_post_request_to_the_book_endpoint(context):
    context.response = do_post_request_to_create_book(context.request_body)


@when('I add a new book using the same {entity} as before')
def when_i_add_another_book_using_the_same_author_but_different_title(context, entity):
    same_entity = context.request_body[f'{entity}']
    context.request_body = get_valid_create_book_payload()
    context.request_body[f'{entity}'] = same_entity
    when_i_do_a_post_request_to_the_book_endpoint(context)


@when('I try to add another book with the same details')
def when_i_try_to_add_another_book_with_the_same_details(context):
    context.response = do_post_request_to_create_book(context.request_body)


# THENs
@then('I receive an error that the book with that name already exists')
def then_i_receive_an_error_that_the_book_with_that_name_already_exists(context):
    assert_that(context.response.status_code).is_equal_to(400)
    assert_that(context.response.json()).is_equal_to(f"Book with name: {context.request_body['name']} writen by author:"
                                                     f" {context.request_body['author']} already exists")
