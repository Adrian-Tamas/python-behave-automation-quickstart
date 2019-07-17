from assertpy import assert_that
from behave import given, when, then

from actions.api.reservation_endpoint_actions import do_post_request_to_create_reservation
from models.endpoints.reservations_model import get_valid_create_reservation_payload
from tests.steps.backend.book.create_book_steps import given_i_have_a_new_book_added_into_database
from tests.steps.backend.user.get_users_steps import given_i_have_a_new_user_added_into_database


@given('I have a new user and book added into database')
def given_i_have_a_new_user_and_book_added_into_database(context):
    given_i_have_a_new_user_added_into_database(context)
    context.user_id = context.response.json()['id']
    context.user = context.response.json()
    given_i_have_a_new_book_added_into_database(context)
    context.book_id = context.response.json()['id']
    context.book = context.response.json()


@given('I have a valid configuration to create a reservation')
def given_i_have_a_valid_configuration_to_create_a_reservation(context):
    context.request_body = get_valid_create_reservation_payload(book_id=context.book_id, user_id=context.user_id)


@when('I do a POST request to the reservation endpoint')
def when_i_do_a_post_request_to_the_reservation_endpoint(context):
    context.response = do_post_request_to_create_reservation(context.request_body)


@when('I try to create another reservation with the same details')
def when_i_try_to_create_another_reservation_with_the_same_details(context):
    when_i_do_a_post_request_to_the_reservation_endpoint(context)


@then('the response will contain the new reservation with the correct details')
def then_the_response_will_contain_the_new_reservation_with_the_correct_details(context):
    assert_that(context.response.json()['user']).is_equal_to(context.user)
    assert_that(context.response.json()['book']).is_equal_to(context.book)
    assert_that(context.response.json()['reservation_date']).is_equal_to(context.request_body['reservation_date'])
    assert_that(context.response.json()['reservation_expiration_date']).is_equal_to(
        context.request_body['reservation_expiration_date'])


@then('I get an error that the reservation already exists')
def then_i_get_an_error_that_the_reservation_already_exists(context):
    assert_that(context.response.status_code).is_equal_to(400)
    assert_that(context.response.json()).is_equal_to(f'Reservation for user: {context.user_id} '
                                                     f'and book: {context.book_id} already exists')
