from behave import given, when, then
from assertpy import assert_that
from pages.reservations.reservations_page import ReservationsPage
from tests.steps.reservations.backend.\
    get_reservations_steps import given_i_already_have_at_least_one_reservation


@given(u'I have at least 1 reservation')
def given_i_have_at_least_one_reservation(context):
    given_i_already_have_at_least_one_reservation(context)


@when(u'I navigate to the reservations page')
def when_i_navigate_to_the_reservations_page(context):
    context.reservations_page = ReservationsPage(context.driver)
    context.driver.get(context.reservations_page.url)


@when(u'I search for a user first name match of {search_term}')
def when_i_search_for_a_user_first_name_mach(context, search_term):
    context.reservations_page.filter_table(search_term)


@when(u"I click on the first reservation row")
def when_i_click_on_the_first_reservations_row(context):
    context.reservations_page.click_on_first_reservations_row()


@when(u"I click delete reservation button")
def when_i_click_delete_reservation_button(context):
    context.reservations_page.click_on_delete_btn()


@when(u"I click edit reservation button")
def when_i_click_edit_reservation_button(context):
    context.reservations_page.click_on_edit_btn()


@when(u"I click create button")
def when_i_click_create_button(context):
    context.reservations_page.click_on_create_btn()


@then(u'I can see a list of all reservations')
def then_i_can_see_a_list_of_all_reservations(context):
    assert_that(context.reservations_page.check_reservations_displayed()).is_equal_to(True)


@then(u"all the reservations displayed will have {search_term} in the name")
def then_reservations_are_filtered(context, search_term):
    assert_that(context.reservations_page.is_text_present_in_all_rows(search_term)).is_true()


@then(u"{buttons} are not clickable")
def then_edit_and_delete_buttons_are_not_clickable(context, buttons):
    print(f"*****__In Then______{buttons}___*******************")
    assert_that(context.reservations_page.is_button_enabled(buttons)).is_equal_to(False)


@then(u"delete reservation appears")
def then_delete_reservation_pop_up_appears(context):
    assert_that(context.reservations_page.is_delete_message_displayed()).is_equal_to(True)


@then(u"I click on cancel deleting")
def then_click_on_cancel_deleting(context):
    context.reservations_page.click_on_cancel_deleting()


@then(u"I click on cancel edit")
def then_click_on_cancel_edit(context):
    context.reservations_page.click_on_cancel_edit()


@then(u"I click on cancel create")
def then_click_on_cancel_create(context):
    context.reservations_page.click_on_cancel_create()


@then(u"edit reservation form appears")
def then_edit_reservation_form_appears(context):
    assert_that(context.reservations_page.is_edit_title_displayed()).is_equal_to(True)


@then(u"create reservation form appears")
def then_create_reservation_form_appears(context):
    assert_that(context.reservations_page.is_create_title_displayed()).is_equal_to(True)



