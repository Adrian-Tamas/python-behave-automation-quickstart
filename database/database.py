from functools import wraps
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from database import logger, Base


def check_session():
    """
    Decorator function to check if the session has been initialized

    :return: callable
    :raises Exception
    """

    def check_session_wrapper(callable_func):
        @wraps(callable_func)
        def decor_inner(instance, *args, **kwargs):
            if not instance.session:
                raise AttributeError('No session. Please use context manager.')
            return callable_func(instance, *args, **kwargs)

        return decor_inner

    return check_session_wrapper


class SQLiteDatabaseConnection:

    def __init__(self):
        # TODO: read the url from config and set up the engine depending on the db type you need
        self.engine = create_engine("sqlite:///db.sqlite", echo=False)
        # engine = create_engine('postgres://user:%s@host/database' % urlquote('badpass'))
        # engine = create_engine(mysql://{}:{}@localhost:3306/test_db'.format(USR, PWD))
        self.session = None
        self.connection_name = None

    """
    Default method to allow the db connection to be used in a context
    """
    def __enter__(self):
        self.session = sessionmaker(bind=self.engine)()

    """
    Default method to allow the db connection to be used in a context
    """
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.session.rollback()
            self.session.close()
            return False
        else:
            try:
                self.session.commit()
            except Exception as err:
                logger.error(f"Commit failed: {err}")
                self.session.rollback()
                self.session.close()
        self.session.close()



