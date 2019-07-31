from collections import namedtuple
from datetime import datetime, timedelta
from random import randint

today = datetime.now()


def _setup_create_reservation(user_id, book_id):
    """
    Create payload to add reservation
    :param user_id: the id of the user
    :param book_id: the id of the book
    :return:
    {
    "book_id":"",
    "user_id":"",
    "reservation_date": "",
    "reservation_expiration_date": ""
    }
    """
    ReservationModel = namedtuple("ReservationModel",
                                  ["book_id", "user_id", "reservation_date", "reservation_expiration_date"])
    return ReservationModel(book_id=book_id,
                            user_id=user_id,
                            reservation_date=today.strftime('%Y-%m-%d'),
                            reservation_expiration_date=(today + timedelta(randint(1, 9))).strftime('%Y-%m-%d'))


def get_valid_create_reservation_payload(book_id, user_id):
    request_body = dict(_setup_create_reservation(user_id=user_id, book_id=book_id)._asdict())
    return request_body
