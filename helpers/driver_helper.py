import sys
from selenium import webdriver


def get_driver(browser: str):
    this_module = sys.modules[__name__]
    if not hasattr(this_module, f"{browser}_driver"):
        available_browsers = [i[:-7] for i in dir(this_module) if i.endswith("_driver") and not i == "get_driver"]
        raise Exception(f"Unsupported driver. Available values for browser: {available_browsers}")
    return getattr(this_module, f"{browser}_driver")()


def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.accept_insecure_certs = True
    options.assume_untrusted_cert_issuer = True
    return webdriver.Chrome(options=options)


def firefox_driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.profile = webdriver.FirefoxProfile()
    firefox_options.profile.set_preference('app.update.auto', False)
    firefox_options.profile.set_preference('app.update.enabled', False)
    return webdriver.Firefox(options=firefox_options)


def edge_driver():
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("--start-maximized")
    return webdriver.Edge(options=edge_options)




