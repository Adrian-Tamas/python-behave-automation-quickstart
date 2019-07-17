import logging

from assertpy import assert_that
from behave import given, when, then

from actions.api.reservation_endpoint_actions import (do_get_request_for_all_reservations,
                                                      do_get_reservation_by_book_id_or_user_id,
                                                      do_get_reservation_by_book_id_and_user_id)
from models.endpoints.reservations_model import get_valid_create_reservation_payload
from tests.steps.backend.book.create_book_steps import given_i_have_a_new_book_added_into_database
from tests.steps.backend.reservation.create_reservation_steps import (
    given_i_have_a_new_user_and_book_added_into_database,
    given_i_have_a_valid_configuration_to_create_a_reservation,
    when_i_do_a_post_request_to_the_reservation_endpoint)

logger = logging.getLogger('python-behave-automation-quickstart')


# GIVENs
@given('I have at least one reservation added into database')
def given_i_have_at_least_one_reservation_added_into_database(context):
    given_i_have_a_new_user_and_book_added_into_database(context)
    given_i_have_a_valid_configuration_to_create_a_reservation(context)
    when_i_do_a_post_request_to_the_reservation_endpoint(context)


@given('I add a new reservation for the same user')
def given_i_add_a_new_reservation_for_the_same_user(context):
    given_i_have_a_new_book_added_into_database(context)
    context.second_book_id = context.response.json()['id']
    context.second_book = context.response.json()
    context.request_body = get_valid_create_reservation_payload(book_id=context.second_book_id, user_id=context.user_id)
    when_i_do_a_post_request_to_the_reservation_endpoint(context)


# WHENs
@when('I do a get all reservations request')
def when_i_do_a_get_all_reservations_request(context):
    context.response = do_get_request_for_all_reservations()


@when('I do a get request for reservation using {param} id')
def when_i_do_a_get_request_for_one_reservation_using_book_id(context, param):
    context.response_after_reservation_created = context.response.json()
    param_id = getattr(context, f'{param}_id')
    context.response = do_get_reservation_by_book_id_or_user_id(param=param, param_id=param_id)


@when('I do the get request for reservation using user_id and book id')
def when_i_do_the_get_request_for_reservation_using_user_id_and_book_id(context):
    context.response_after_reservation_created = context.response.json()
    context.response = do_get_reservation_by_book_id_and_user_id(user_id=context.user_id, book_id=context.book_id)


# THENs
@then('I should receive a 200 response code and a reservation has the correct attributes')
def then_i_should_receive_a_200_response_code_and_a_reservation_has_the_correct_attributes(context):
    assert_that(context.response.status_code).is_equal_to(200)
    assert_that(context.response.json()).is_type_of(list)
    assert_that(context.response.json()[0]).contains('user', 'book', 'reservation_date', 'reservation_expiration_date')


@then('I get the correct details of that reservation')
def then_i_get_the_correct_details_of_that_reservation(context):
    assert_that(context.response.status_code).is_equal_to(200)
    if type(context.response.json()) == list:
        assert_that(context.response.json()[0]).is_equal_to(context.response_after_reservation_created)
    else:
        assert_that(context.response.json()).is_equal_to(context.response_after_reservation_created)


@then('I get the details of all reservations that a user has in database')
def then_i_get_the_details_of_all_reservations_that_a_user_has_in_database(context):
    assert_that(context.response.status_code).is_equal_to(200)
    assert_that(context.response.json()[0]['user']).is_equal_to(context.user)
    assert_that(context.response.json()[1]['user']).is_equal_to(context.user)
    assert_that(context.response.json()[0]['book']).is_equal_to(context.book)
    assert_that(context.response.json()[1]['book']).is_equal_to(context.second_book)
