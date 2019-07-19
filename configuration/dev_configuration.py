import configparser


class DevConfiguration:
    ENV_NAME = "default"

    def __init__(self):
        self.configuration = configparser.ConfigParser(allow_no_value=True)
        self.configuration.read("dev_configuration.ini")
        self.backend_url = self.configuration[self.ENV_NAME]["backend_url"]
        self.frontend_url = self.configuration[self.ENV_NAME]["frontend_url"]
        self.rp_endpoint = self.configuration[self.ENV_NAME]["rp_endpoint"]
        self.rp_project = self.configuration[self.ENV_NAME]["rp_project"]
        self.max_timeout = int(self.configuration[self.ENV_NAME]["max_timeout"])
        self.local = self.configuration[self.ENV_NAME]["local"]

    def read_configuration(self):
        pass
