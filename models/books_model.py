from collections import namedtuple

from models import fake


def _setup_create_book():
    """
    Create payload to Add Book
    :return:
    {
    "name": "Unknown",
    "author": "Unknown",
    "description": "paragraph",
    "cover": "link to cover picture"
    }
    """
    BookModel = namedtuple("BookModel", ["name", "author", "description", "cover"])
    return BookModel(name=fake.text(20),
                     author=fake.name(),
                     description=fake.paragraph(nb_sentences=6),
                     cover="https://timedotcom.files.wordpress.com/2015/06/521811839-copy.jpg")


def get_valid_with_all_params_create_book_payload():
    request_body = dict(_setup_create_book()._asdict())
    return request_body


def get_valid_minim_required_create_book_payload():
    request_body = dict(_setup_create_book()._asdict())
    del request_body['description']
    del request_body['cover']
    return request_body


def get_add_book_payload_without_parameter(param):
    request_body = dict(_setup_create_book()._asdict())
    del request_body[param]
    return request_body
