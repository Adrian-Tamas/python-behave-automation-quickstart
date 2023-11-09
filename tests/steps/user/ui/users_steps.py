from assertpy import assert_that
from behave import given, when, then
from pages.users.users_page import UsersPage
from faker import Faker

from pages.users.create_user_page import CreateUserPage
from tests.steps.user.backend.create_user_steps import (given_i_have_a_correct_user_payload,
                                                        when_i_do_a_post_request_to_the_user_endpoint)

fake = Faker()

@given(u'I have at least 1 user')
def given_i_have_at_least_one_user(context):
    given_i_have_a_correct_user_payload(context)
    when_i_do_a_post_request_to_the_user_endpoint(context)

@when(u'I navigate to the users page')
def when_i_navigate_to_the_users_page(context):
    context.users_page = UsersPage(context.driver)
    context.driver.get(context.users_page.url)

@then(u'I can see a list of available users')
def then_i_can_see_a_list_of_available_users(context):
    assert_that(context.users_page.check_users_displayed()).is_true()

@given(u'I have details for a new user')
def given_i_have_details_for_a_new_user(context):
    context.user = {
        "first_name": fake.name(),
        "last_name": fake.name(),
        "email": fake.email()
    }
@given(u'I open the create users page')
def given_i_open_the_create_users_page(context):
    users_page = UsersPage(context.driver)
    context.driver.get(users_page.url)
    context.create_user_page = users_page.open_create_users(CreateUserPage)

@when(u'I enter the details and save the user details')
def when_i_enter_the_details_and_save_the_user(context):
    context.users_page = context.create_user_page.fill_in_user_details(context.user).click_save_user_button(UsersPage)

@when(u"I search for a partial user match of '{search_term}'")
def when_i_search_for_a_partial_title_match(context, search_term):
    context.users_page.filter_table(search_term)

@when(u'I open the user details')
def when_i_open_the_user_details(context):
    user_id = context.response.json()['id']
    context.details_modal = context.users_page.open_user_details(user_id)

@then(u'all the expected user details are present')
def then_all_the_expected_details_are_present(context):
    user = context.response.json()
    user_details_modal = context.details_modal
    assert_that(user_details_modal.check_modal_is_displayed()).is_true()
    assert_that(user_details_modal.check_modal_title()).is_true()
    assert_that(user_details_modal.check_user_details(user)).is_true()


@then(u"all the users displayed will have '{search_term}' in the name")
def then_users_are_filtered(context, search_term):
    assert_that(context.users_page.is_text_present_in_all_rows(search_term)).is_true()


@then(u'the user is saved')
def then_the_user_is_saved(context):
    full_name = context.user.get("first_name") + " " + context.user.get("last_name")
    assert_that(context.users_page.is_success_message_displayed(full_name)).is_true()
    assert_that(context.users_page.is_user_present_on_page(context.user)).is_true()


