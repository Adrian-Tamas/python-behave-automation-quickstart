import configparser


class TestConfiguration:
    ENV_NAME = "default"

    def __init__(self):
        self.configuration = configparser.ConfigParser(allow_no_value=True)
        self.configuration.read("test_config.ini")
        self.backend_url = self.configuration[self.ENV_NAME]["backend_url"]
        self.rp_endpoint = self.configuration[self.ENV_NAME]["rp_endpoint"]
        self.rp_project = self.configuration[self.ENV_NAME]["rp_project"]