import importlib
import json
import logging.config
import os

env = os.environ.get("env", "dev")

supported_envs = ["dev", "test"]


def __init_logging():
    path = 'logging.json'
    if os.path.exists(path):
        with open(path, 'rt') as file:
            logging.config.dictConfig(json.loads(file.read()))
    else:
        logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s - %(module)s::%(funcName)s - [%(levelname)s] - %(message)s")


__init_logging()

if env not in supported_envs:
    raise EnvironmentError("Unsupported environment: " + env)
module = importlib.import_module(f'configuration.{env}_configuration')
class_name = f'{env}Configuration'

class_attr = None
for attr in dir(module):
    if attr.lower() == class_name.lower():
        class_attr = attr
if not class_attr:
    raise ValueError(f'configuration class not found for env {env}')
configuration = getattr(module, class_attr)()

configuration.read_configuration()

local = configuration.local
backend_url = configuration.backend_url
frontend_url = configuration.frontend_url
rp_endpoint = configuration.rp_endpoint
rp_project = configuration.rp_project
max_timeout = configuration.max_timeout
