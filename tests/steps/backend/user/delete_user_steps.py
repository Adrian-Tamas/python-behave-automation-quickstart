from assertpy import assert_that
from behave import given, when, then

from actions.api.user_endpoint_actions import do_delete_request_for_user


# GIVENs
@given('I have the related user id')
def given_i_have_the_related_user_id(context):
    context.user_id = context.response.json()['id']


# WHENs
@when('I do a DELETE request to the user endpoint')
def when_i_do_a_delete_request_to_the_users_endpoint(context):
    context.response = do_delete_request_for_user(context.user_id)


@when('I do a DELETE request to the user endpoint with that ID')
def when_i_do_a_delete_request_to_the_user_endpoint_with_that_id(context):
    context.response = do_delete_request_for_user(context.not_existing_user_id)


# THENs
@then('I successfully deleted the user')
def then_i_successfully_deleted_the_user(context):
    assert_that(context.response.status_code).is_equal_to(200)
    assert_that(context.response.json()).is_equal_to(f'Successfully deleted user {context.user_id}')
    context.user_ids.remove(context.user_id)
