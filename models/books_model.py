from collections import namedtuple
from faker import Faker

from configuration.configuration import local

fake = Faker(local)


def _setup_create_book():
    """
    Create payload to Add Book
    :return:
    {
    "name": "Unknown",
    "author": "Unknown"
    }
    """
    BookModel = namedtuple("BookModel", ["name", "author"])
    return BookModel(name=fake.text(20), author=fake.name())


def get_valid_create_book_payload():
    request_body = dict(_setup_create_book()._asdict())
    return request_body


def get_add_book_payload_without_parameter(param):
    request_body = dict(_setup_create_book()._asdict())
    del request_body[param]
    return request_body
