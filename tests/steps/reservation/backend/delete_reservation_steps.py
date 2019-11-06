import uuid

from assertpy import assert_that
from behave import given, when, then

from actions.api.reservation_endpoint_actions import (do_delete_reservation_by_book_id_or_user_id,
                                                      do_delete_reservation_by_book_id_and_user_id)
from tests.steps.user.backend import given_i_add_a_new_user


# GIVENs
@given('I already added a user')
def given_i_already_added_a_user(context):
    given_i_add_a_new_user(context)
    context.user_id = context.response.json()['id']


# WHENs
@when('I do a delete request for reservation using book id')
def when_i_do_a_delete_request_for_reservation_using_book_id(context):
    context.entity = "book"
    context.id = context.book_id
    context.response = do_delete_reservation_by_book_id_or_user_id(book_id=context.id)


@when('I do a delete request for reservation using user id')
def when_i_do_a_delete_request_for_reservation_using_user_id(context):
    context.entity = "user"
    context.id = context.user_id
    context.response = do_delete_reservation_by_book_id_or_user_id(user_id=context.id)


@when('I try to delete reservation using wrong book id')
def when_i_do_a_delete_request_for_reservation_using_wrong_book_id(context):
    context.book_id = str(uuid.uuid4())
    context.response = do_delete_reservation_by_book_id_and_user_id(user_id=context.user_id, book_id=context.book_id)


@when('I try to delete reservation using wrong user id')
def when_i_do_a_delete_request_for_reservation_using_wrong_user_id(context):
    context.user_id = str(uuid.uuid4())
    context.response = do_delete_reservation_by_book_id_and_user_id(user_id=context.user_id, book_id=context.book_id)


# THENs
@then('I successfully deleted the reservation')
def then_i_deleted_successfully_the_reservation(context):
    assert_that(context.response.status_code).is_equal_to(200)
    assert_that(context.response.json()).is_equal_to(f'Deleted reservation for {context.entity} {context.id}')


@then('I successfully deleted reservation for user')
def then_i_successfully_deleted_reservation_for_user(context):
    assert_that(context.response.status_code).is_equal_to(200)
    assert_that(context.response.json()).is_equal_to(f'Deleted 1 of reservations for '
                                                     f'{context.entity}s {context.id}')


@then("I get an error that the reservation wasn't found")
def then_i_get_an_error_that_the_reservation_wasn_t_found(context):
    assert_that(context.response.status_code).is_equal_to(400)
    assert_that(context.response.json()).is_equal_to(f"Reservation with (user_id, book_id) = "
                                                     f"('{context.user_id}', '{context.book_id}') was not found")
