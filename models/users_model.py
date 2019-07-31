from collections import namedtuple

from models import fake


def _setup_create_user():
    """
    Create the payload to Add User
    :return:
    {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@someemail.com"
    }
    """
    UserModel = namedtuple("UsersModel", ["first_name", "last_name", "email"])
    return UserModel(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email())


def get_valid_create_user_payload():
    request_body = dict(_setup_create_user()._asdict())
    return request_body


def get_add_user_payload_without_parameter(param):
    request_body = dict(_setup_create_user()._asdict())
    del request_body[param]
    return request_body
