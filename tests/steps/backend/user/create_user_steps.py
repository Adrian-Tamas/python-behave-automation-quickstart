from assertpy import assert_that
from behave import given, when, then

from actions.api.user_endpoint_actions import do_post_request_to_create_user
from models.users_model import get_valid_create_user_payload, get_add_user_payload_without_parameter


# GIVENs
@given('I have a correct User payload')
def given_i_have_a_correct_user_payload(context):
    context.request_body = get_valid_create_user_payload()


@given('I have an User payload without {param}')
def given_i_have_an_user_payload_without_param(context, param):
    context.request_body = get_add_user_payload_without_parameter(param=param)


@given('I have an User payload with invalid email format')
def given_i_have_an_user_payload_with_invalid_email_format(context):
    context.request_body = get_valid_create_user_payload()
    context.request_body['email'] = context.request_body['email'].replace('@', '')


# WHENs
@when('I do a POST request to the user endpoint')
def when_i_do_a_post_request_to_the_user_endpoint(context):
    context.response = do_post_request_to_create_user(context.request_body)


@when('I try to add another user with the same email address')
def when_i_try_to_add_another_user_with_the_same_email_address(context):
    context.same_email = context.request_body['email']
    context.new_request_body = get_valid_create_user_payload()
    context.new_request_body['email'] = context.same_email
    context.response = do_post_request_to_create_user(context.new_request_body)


# THENs
@then('the request will be successful with 200 response code')
def then_the_request_will_be_successful_with_200_response_code(context):
    assert_that(context.response.status_code).is_equal_to(200)


@then('the response will contain the new object with the related ID')
def then_the_response_will_contain_the_new_object_with_the_related_id(context):
    json = context.response.json()
    assert_that(json).is_equal_to(context.request_body, ignore=["id", "description", "cover"])
    assert_that(json['id']).is_type_of(str).is_length(36)


@then('I receive an error that the email address already exists')
def then_i_receive_an_error_that_the_email_address_already_exists(context):
    assert_that(context.response.status_code).is_equal_to(400)
    assert_that(context.response.json()).is_equal_to(f'User with email: {context.same_email} already exists')


@then('I receive an error that the {param} is {reason}')
def then_i_receive_an_error_that_the_param_is_required(context, param, reason):
    assert_that(context.response.status_code).is_equal_to(400)
    assert_that(context.response.json()).is_equal_to(f"'{param}' is {reason}")
