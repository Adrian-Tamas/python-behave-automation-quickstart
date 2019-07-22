import uuid

from assertpy import assert_that
from behave import given, when, then
from faker import Faker

from actions.api.reservation_endpoint_actions import do_put_request_to_update_reservation
from configuration.configuration import local

fake = Faker(local)


# GIVENs
@given('I want to change the reservation dates')
def given_i_want_to_change_the_reservation_dates(context):
    context.request_body['reservation_date'] = fake.date(pattern="%Y-%m-%d", end_datetime=None)
    context.request_body['reservation_expiration_date'] = fake.date(pattern="%Y-%m-%d", end_datetime=None)


@given('I want to change the reservation dates using not existing {param}')
def given_i_want_to_change_the_reservation_dates_using_not_existing_user_id(context, param):
    given_i_want_to_change_the_reservation_dates(context)
    context.request_body[param] = str(uuid.uuid4())


# WHENs
@when('I do a PUT request to the reservation endpoint')
def when_i_do_a_put_request_to_the_reservation_endpoint(context):
    context.response = do_put_request_to_update_reservation(user_id=context.user_id,
                                                            book_id=context.book_id,
                                                            reservation=context.request_body)


# THENs
@then('the response is with success and the updated reservation details are displayed')
def then_the_response_is_with_success_and_the_updated_reservation_details_are_displayed(context):
    json = context.response.json()
    assert_that(context.response.status_code).is_equal_to(200)
    assert_that(json['reservation_date']).is_equal_to(context.request_body['reservation_date'])
    assert_that(json['reservation_expiration_date']).is_equal_to(context.request_body['reservation_expiration_date'])


@then('I get an error that the reservation that I want to edit is invalid')
def then_i_get_an_error_that_the_reservation_that_i_want_to_edit_is_invalid(context):
    assert_that(context.response.status_code).is_equal_to(400)
    assert_that(context.response.json()).is_equal_to(f'Reservation for user: {context.user_id} '
                                                     f'and book: {context.book_id} is invalid')
