import os

from elementium.drivers.se import SeElements
from reportportal_behave.behave_integration_service import BehaveIntegrationService

from configuration.configuration import rp_endpoint, rp_project

from helpers.driver_helper import get_driver


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
