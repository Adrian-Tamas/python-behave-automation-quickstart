import uuid

from assertpy import assert_that
from behave import given, when, then

from actions.api.user_endpoint_actions import do_get_request_for_all_users, do_get_request_for_user
from tests.steps.backend.user.create_user_steps import (given_i_have_a_correct_user_payload,
                                                        when_i_do_a_post_request_to_the_user_endpoint)


# GIVENs
@given('I already have at least one user')
def given_i_already_have_at_least_one_user(context):
    given_i_have_a_correct_user_payload(context)
    when_i_do_a_post_request_to_the_user_endpoint(context)


@given('I get the number of existing users')
def given_i_get_the_number_of_existing_users(context):
    all_users_response = do_get_request_for_all_users()
    context.number_of_users_before = len(all_users_response.json())


@given('I already have a new user')
def given_i_already_have_a_new_user(context):
    given_i_have_a_correct_user_payload(context)
    when_i_do_a_post_request_to_the_user_endpoint(context)


@given("I have an user_id for an user that doesn't exist")
def given_i_have_an_user_id_for_an_user_that_does_not_exist(context):
    context.not_existing_user_id = str(uuid.uuid4())


# WHENs
@when('I do a get all users request')
def when_i_do_a_get_all_users_request(context):
    context.all_users_response = do_get_request_for_all_users()


@when('I get the number of users')
def when_i_get_the_number_of_users(context):
    all_users_response = do_get_request_for_all_users()
    context.number_of_users_after = len(all_users_response.json())


@when('I do a get request for one user with correct user_id')
def when_i_do_a_get_request_for_one_user_with_correct_user_id(context):
    context.valid_user_id = context.response.json()['id']
    context.response = do_get_request_for_user(user_id=context.valid_user_id)


@when('I do a get request for one user with that user_id')
def when_i_do_a_get_request_for_one_user_with_that_user_id(context):
    context.response = do_get_request_for_user(user_id=context.not_existing_user_id)


# THENs
@then('I should receive a 200 response code and an item has the correct attributes')
def then_i_should_receive_a_200_response_code_and_an_item_has_the_correct_attributes(context):
    assert_that(context.all_users_response.status_code).is_equal_to(200)
    assert_that(context.all_users_response.json()[0]).contains('id', 'first_name', 'last_name', 'email')


@then('in the end the list of users is larger with one item')
def then_in_the_end_the_list_of_users_is_larger_with_one_item(context):
    assert_that(context.number_of_users_after).is_equal_to(context.number_of_users_before + 1)


@then('the related user payload is successfully displayed')
def then_the_related_user_payload_is_successfully_displayed(context):
    json = context.response.json()
    assert_that(context.response.status_code).is_equal_to(200)
    assert_that(json['id']).is_equal_to(context.valid_user_id)
    assert_that(json).is_equal_to(context.request_body, ignore='id')


@then('I receive an error that the user was not found')
def then_i_receive_an_error_that_the_user_was_not_found(context):
    assert_that(context.response.status_code).is_equal_to(400)
    assert_that(context.response.json()).is_equal_to(f'User with user_id = {context.not_existing_user_id} '
                                                     f'was not found')
