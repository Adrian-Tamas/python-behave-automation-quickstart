from assertpy import assert_that
from behave import given, when, then

from actions.api.reservation_endpoint_actions import (do_get_request_for_all_reservations,
                                                      do_get_reservation_by_entity_id,
                                                      do_get_reservation_by_book_id_and_user_id)
from models.reservations_model import get_valid_create_reservation_payload
from tests.steps.book.backend.create_book_steps import given_i_already_have_a_book_only_with_the_required_parameters
from tests.steps.reservations.backend.create_reservation_steps import (given_i_already_have_an_user_and_a_book,
                                                                       given_i_have_a_valid_payload_to_create_a_reservation,
                                                                       when_i_do_a_post_request_to_the_reservation_endpoint)


# GIVENs
@given('I already have at least one reservation')
def given_i_already_have_at_least_one_reservation(context):
    given_i_already_have_an_user_and_a_book(context)
    given_i_have_a_valid_payload_to_create_a_reservation(context)
    when_i_do_a_post_request_to_the_reservation_endpoint(context)


@given('I add a new reservation for the same user')
def given_i_add_a_new_reservation_for_the_same_user(context):
    given_i_already_have_a_book_only_with_the_required_parameters(context)
    context.second_book_id = context.response.json()['id']
    context.second_book = context.response.json()
    context.request_body = get_valid_create_reservation_payload(book_id=context.second_book_id, user_id=context.user_id)
    when_i_do_a_post_request_to_the_reservation_endpoint(context)


# WHENs
@when('I do a get all reservations request')
def when_i_do_a_get_all_reservations_request(context):
    context.response = do_get_request_for_all_reservations()


@when('I do a get request for reservation using book id')
def when_i_do_a_get_request_for_one_reservation_using_book_id(context):
    context.response_after_reservation_created = context.response.json()
    context.response = do_get_reservation_by_entity_id(book_id=context.book_id)


@when('I do a get request for reservation using user id')
def when_i_do_a_get_request_for_one_reservation_using_user_id(context):
    context.response_after_reservation_created = context.response.json()
    context.response = do_get_reservation_by_entity_id(user_id=context.user_id)


@when('I do the get request for reservation using user_id and book id')
def when_i_do_the_get_request_for_reservation_using_user_id_and_book_id(context):
    context.response_after_reservation_created = context.response.json()
    context.response = do_get_reservation_by_book_id_and_user_id(user_id=context.user_id, book_id=context.book_id)


# THENs
@then('I should receive a 200 response code and a reservation has the correct attributes')
def then_i_should_receive_a_200_response_code_and_a_reservation_has_the_correct_attributes(context):
    reservation_list = context.response.json()
    assert_that(context.response.status_code).is_equal_to(200)
    assert_that(reservation_list).is_type_of(list)
    assert_that(reservation_list[0]).contains('user', 'book', 'reservation_date', 'reservation_expiration_date')


@then('I get the correct details of that reservation')
def then_i_get_the_correct_details_of_that_reservation(context):
    reservation_response = context.response.json()
    assert_that(context.response.status_code).is_equal_to(200)
    if type(reservation_response) == list:
        assert_that(reservation_response[0]).is_equal_to(context.response_after_reservation_created)
    else:
        assert_that(reservation_response).is_equal_to(context.response_after_reservation_created)


@then('I get the details of all reservations that a user has')
def then_i_get_the_details_of_all_reservations_that_a_user_has(context):
    reservation1, reservation2 = context.response.json()
    assert_that(context.response.status_code).is_equal_to(200)
    assert_that(reservation1).has_user(context.user).has_book(context.book)
    assert_that(reservation2).has_user(context.user).has_book(context.second_book)