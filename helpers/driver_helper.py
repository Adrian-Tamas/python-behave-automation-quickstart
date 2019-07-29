import os
from tokenize import String

import sys

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


def get_root_dir():
    """ Getting the root dir of the project"""
    return os.getcwd()


def get_driver(browser: String):
    this_module = sys.modules[__name__]
    if not hasattr(this_module, f"{browser}_driver"):
        # get list of methods that end with driver except the current one, remove the trailing _driver to print them
        available_browsers = [i[:-7] for i in dir(this_module) if i.endswith("_driver") and not i == "get_driver"]
        raise Exception(f"Unsupported driver. Available values for browser: {available_browsers}")
    return getattr(this_module, f"{browser}_driver")()


def chrome_driver():
    driver_path = os.path.join(get_root_dir(), 'static_resources', 'drivers', 'windows', 'chromedriver.exe')
    caps = DesiredCapabilities.CHROME
    caps['acceptSslCerts'] = True
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.accept_untrusted_certs = True
    options.assume_untrusted_cert_issuer = True
    return webdriver.Chrome(options=options,
                            desired_capabilities=caps,
                            executable_path=driver_path)


def firefox32_driver():
    # TODO: make this work with 32 bit
    driver_path = os.path.join(get_root_dir(), 'static_resources', 'drivers', 'windows', 'geckodriver_win32.exe')
    caps = DesiredCapabilities.FIREFOX
    caps["marionette"] = True
    caps['acceptSslCerts'] = True

    profile = webdriver.FirefoxProfile()
    profile.set_preference('app.update.auto', False)
    profile.set_preference('app.update.enabled', False)
    return webdriver.Firefox(profile,
                             capabilities=caps,
                             executable_path=driver_path)


def firefox64_driver():
    driver_path = os.path.join(get_root_dir(), 'static_resources', 'drivers', 'windows', 'geckodriver_win64.exe')
    caps = DesiredCapabilities.FIREFOX
    caps["marionette"] = True
    caps['acceptSslCerts'] = True

    profile = webdriver.FirefoxProfile()
    profile.set_preference('app.update.auto', False)
    profile.set_preference('app.update.enabled', False)
    return webdriver.Firefox(profile,
                             capabilities=caps,
                             executable_path=driver_path)
