from assertpy import assert_that
from behave import given, when, then, step

from actions.api.reservation_endpoint_actions import do_post_request_to_create_reservation
from models.reservations_model import get_valid_create_reservation_payload
from tests.steps.book.backend.create_book_steps import given_i_already_have_a_book_only_with_the_required_parameters
from tests.steps.user.backend.get_users_steps import given_i_add_a_new_user


# GIVENs
@given('I already have an user and a book')
def given_i_already_have_an_user_and_a_book(context):
    given_i_add_a_new_user(context)
    context.user_id = context.response.json()['id']
    context.user = context.response.json()
    given_i_already_have_a_book_only_with_the_required_parameters(context)
    context.book_id = context.response.json()['id']
    context.book = context.response.json()


@given('I have a valid payload to create a reservations')
def given_i_have_a_valid_payload_to_create_a_reservation(context):
    context.request_body = get_valid_create_reservation_payload(book_id=context.book_id, user_id=context.user_id)


# WHENs
@step('I do a POST request to the reservations endpoint')
def when_i_do_a_post_request_to_the_reservation_endpoint(context):
    context.response = do_post_request_to_create_reservation(context.request_body)


@when('I try to create another reservations with the same details')
def when_i_try_to_create_another_reservation_with_the_same_details(context):
    when_i_do_a_post_request_to_the_reservation_endpoint(context)


# THENs
@then('the response will contain the new reservations with the correct details')
def then_the_response_will_contain_the_new_reservation_with_the_correct_details(context):
    reservation = context.response.json()
    assert_that(reservation) \
        .has_user(context.user) \
        .has_book(context.book) \
        .has_reservation_date(context.request_body['reservation_date']) \
        .has_reservation_expiration_date(context.request_body['reservation_expiration_date'])


@then('I get an error that the reservations already exists')
def then_i_get_an_error_that_the_reservation_already_exists(context):
    assert_that(context.response.status_code).is_equal_to(400)
    assert_that(context.response.json()).is_equal_to(f'Reservation for user: {context.user_id} '
                                                     f'and book: {context.book_id} already exists')
