import assertpy
import logging
import os

from elementium.drivers.se import SeElements
import assertpy
from reportportal_behave.behave_integration_service import BehaveIntegrationService

from actions.api.book_endpoint_actions import do_delete_request_for_book
from actions.api.user_endpoint_actions import do_delete_request_for_user
from configuration.configuration import rp_endpoint, rp_project
from helpers.driver_helper import get_driver

logger = logging.getLogger('default')


def before_all(context):
    rp_enable = context.config.userdata.getbool('rp_enable', False)
    step_based = context.config.userdata.getbool('step_based', False)
    context.requested_browser = context.config.userdata.get('browser', "chrome")
    rp_token = os.environ.get("RP_TOKEN")
    add_screenshot = context.config.userdata.getbool('add_screenshot', False)
    launch_name = f"Execution using tags: {context.config.tags.ands[0]}"
    launch_description = f"BDD Tests for: {', '.join(tag for tag in context.config.tags.ands[0])}"
    context.behave_integration_service = BehaveIntegrationService(rp_endpoint=rp_endpoint,
                                                                  rp_project=rp_project,
                                                                  rp_token=rp_token,
                                                                  rp_launch_name=launch_name,
                                                                  rp_launch_description=launch_description,
                                                                  rp_enable=rp_enable,
                                                                  step_based=step_based,
                                                                  add_screenshot=add_screenshot)
    context.behave_integration_service.launch_service(context.config.tags.ands[0])
    context.book_ids = []
    context.user_ids = []


def before_feature(context, feature):
    context.behave_integration_service.before_feature(feature)
    if 'ui' in feature.tags:
        context.driver = get_driver(context.requested_browser)
        context.timeout = 10
        context.browser = SeElements(context.driver)


def before_scenario(context, scenario):
    context.behave_integration_service.before_feature(scenario)


def before_step(context, step):
    context.behave_integration_service.before_step(step)


def after_step(context, step):
    context.behave_integration_service.after_step(step)


def after_scenario(context, scenario):
    context.behave_integration_service.after_scenario(scenario)


def after_feature(context, feature):
    context.behave_integration_service.after_feature(feature)
    if 'ui' in feature.tags:
        context.driver.quit()


def after_all(context):
    try:
        context.behave_integration_service.after_all()
    except AttributeError:
        pass

    all_book_ids_deleted = True
    all_user_ids_deleted = True

    for book_id in context.book_ids:
        response = do_delete_request_for_book(book_id)
        if not response.ok:
            all_book_ids_deleted = False
    assertpy.assert_that(all_book_ids_deleted).described_as("Not all books were deleted").is_true()

    for user_id in context.user_ids:
        response = do_delete_request_for_user(user_id)
        if not response.ok:
            all_user_ids_deleted = False
    assertpy.assert_that(all_user_ids_deleted).described_as("Not all users were deleted").is_true()
