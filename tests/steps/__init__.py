import logging

from faker import Faker
from configuration.configuration import local

fake = Faker(local)
logger = logging.getLogger('default')
