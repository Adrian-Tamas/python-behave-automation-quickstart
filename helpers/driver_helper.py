import sys

from pygeckodriver import geckodriver_path
from pychromedriver import chromedriver_path
from tokenize import String
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


def get_driver(browser: String):
    this_module = sys.modules[__name__]
    if not hasattr(this_module, f"{browser}_driver"):
        # get list of methods that end with driver except the current one, remove the trailing _driver to print them
        available_browsers = [i[:-7] for i in dir(this_module) if i.endswith("_driver") and not i == "get_driver"]
        raise Exception(f"Unsupported driver. Available values for browser: {available_browsers}")
    return getattr(this_module, f"{browser}_driver")()


def chrome_driver():
    caps = DesiredCapabilities.CHROME
    caps['acceptSslCerts'] = True
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.accept_untrusted_certs = True
    options.assume_untrusted_cert_issuer = True
    return webdriver.Chrome(options=options,
                            desired_capabilities=caps,
                            executable_path=chromedriver_path)


def firefox_driver():
    caps = DesiredCapabilities.FIREFOX
    caps["marionette"] = True
    caps['acceptSslCerts'] = True

    profile = webdriver.FirefoxProfile()
    profile.set_preference('app.update.auto', False)
    profile.set_preference('app.update.enabled', False)
    return webdriver.Firefox(profile,
                             capabilities=caps,
                             executable_path=geckodriver_path)
