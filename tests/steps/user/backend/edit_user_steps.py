from assertpy import assert_that
from behave import given, when, then

from actions.api.user_endpoint_actions import do_put_request_to_update_user
from tests.steps import fake


# GIVENs
@given('I want to change the first and last name')
def given_i_want_to_change_the_first_and_last_name(context):
    context.new_first_name = fake.first_name()
    context.new_last_name = fake.last_name()
    context.request_body['first_name'] = context.new_first_name
    context.request_body['last_name'] = context.new_last_name


@given('I want to assign a new email address to that user')
def given_i_want_to_assign_a_new_email_address_to_that_user(context):
    context.request_body['email'] = fake.email()


# WHENs
@when('I do a PUT request to the user endpoint')
def when_i_do_a_put_request_to_the_user_endpoint(context):
    context.user_id = context.response.json()['id']
    context.response = do_put_request_to_update_user(user_id=context.user_id, user=context.request_body)


# THENs
@then('the response is with success and the updated user details are displayed')
def then_the_response_is_with_success_and_the_updated_user_details_are_displayed(context):
    user = context.response.json()
    request = context.request_body
    assert_that(context.response.status_code).is_equal_to(200)
    assert_that(user) \
        .has_id(context.user_id) \
        .has_first_name(request['first_name']) \
        .has_last_name(request['last_name']) \
        .has_email(request['email'])


@then('I receive the error that the email address is invalid and the user details will not be updated')
def then_i_receive_the_error_that_the_email_address_is_invalid_and_the_user_details_will_not_be_updated(context):
    assert_that(context.response.status_code).is_equal_to(400)
    assert_that(context.response.json()).is_equal_to(f"'email' is invalid")
