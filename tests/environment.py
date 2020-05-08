import logging
import os

from elementium.drivers.se import SeElements
from reportportal_behave.behave_integration_service import BehaveIntegrationService

from configuration.configuration import rp_endpoint, rp_project
from helpers.driver_helper import get_driver

logger = logging.getLogger('default')


def before_all(context):
    tags = ', '.join([tag for tags in context.config.tags.ands for tag in tags])
    rp_enable = context.config.userdata.getbool('rp_enable', False)
    step_based = context.config.userdata.getbool('step_based', True)
    context.requested_browser = context.config.userdata.get('browser', "chrome")
    rp_token = os.environ.get("RP_TOKEN")
    add_screenshot = context.config.userdata.getbool('add_screenshot', False)
    launch_name = f"Execution using tags: {tags}"
    launch_description = f"BDD Tests for: {tags}"
    context.behave_integration_service = BehaveIntegrationService(rp_endpoint=rp_endpoint,
                                                                  rp_project=rp_project,
                                                                  rp_token=rp_token,
                                                                  rp_launch_name=launch_name,
                                                                  rp_launch_description=launch_description,
                                                                  rp_enable=rp_enable,
                                                                  step_based=step_based,
                                                                  add_screenshot=add_screenshot,
                                                                  verify_ssl=False)
    context.launch_id = context.behave_integration_service.launch_service(tags=tags)


def before_feature(context, feature):
    context.feature_id = context.behave_integration_service.before_feature(feature)
    if 'ui' in feature.tags:
        context.driver = get_driver(context.requested_browser)
        context.timeout = 10
        context.browser = SeElements(context.driver)


def before_scenario(context, scenario):
    context.scenario_id = context.behave_integration_service.before_scenario(scenario,
                                                                             feature_id=context.feature_id)


def before_step(context, step):
    context.step_id = context.behave_integration_service.before_step(step, scenario_id=context.scenario_id)


def after_step(context, step):
    context.behave_integration_service.after_step(step, context.step_id)


def after_scenario(context, scenario):
    context.behave_integration_service.after_scenario(scenario, context.scenario_id)


def after_feature(context, feature):
    context.behave_integration_service.after_feature(feature, context.feature_id)
    if 'ui' in feature.tags:
        context.driver.quit()


def after_all(context):
    try:
        context.behave_integration_service.after_all(context.launch_id)
    except AttributeError:
        pass

