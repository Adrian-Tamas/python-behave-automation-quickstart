import logging

from sqlalchemy.ext.declarative import declarative_base

logger = logging.getLogger('default')

Base = declarative_base()
