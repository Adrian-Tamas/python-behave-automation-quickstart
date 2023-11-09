import uuid
from functools import wraps
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import logger
from database.models.database.books_db_model import BooksDBModel
from database.models.database.reservations_db_model import ReservationsDBModel
from database.models.database.users_db_model import UsersDBModel
import os


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
        self.engine = create_engine(f"sqlite:///{os.path.join(os.path.dirname(os.getcwd()), 'pythonlibrarybackend')}\\db.sqlite", echo=False)
        # engine = create_engine('postgres://user:%s@host/database' % urlquote('badpass'))
        # engine = create_engine(mysql://{}:{}@localhost:3306/test_db'.format(USR, PWD))
        self.session = None
        self.connection_name = None

    def __enter__(self):
        self.session = sessionmaker(bind=self.engine)()

    @check_session()
    def add_user(self, user_model: UsersDBModel):
        user_id = str(uuid.uuid4())
        user_model.id = user_id
        self.session.add(user_model)

    @check_session()
    def add_book(self, book_model: BooksDBModel):
        book_id = str(uuid.uuid4())
        book_model.id = book_id
        self.session.add(book_model)

    @check_session()
    def add_reservation(self, reservation_model: ReservationsDBModel):
        self.session.add(reservation_model)

    @check_session()
    def get_all_users(self):
        return self.session.query(UsersDBModel).all()

    @check_session()
    def get_users_by_first_and_last_name(self, first_name, last_name):
        return self.session.query(UsersDBModel) \
            .filter(UsersDBModel.first_name == first_name,
                    UsersDBModel.last_name == last_name).all()

    @check_session()
    def get_user_by_id(self, user_id):
        return self.session.query(UsersDBModel) \
            .filter(UsersDBModel.id == user_id).one_or_none()

    @check_session()
    def get_user_by_email(self, email):
        return self.session.query(UsersDBModel).filter(UsersDBModel.email == email).one_or_none()

    @check_session()
    def get_all_books(self):
        return self.session.query(BooksDBModel).all()

    @check_session()
    def get_book_by_id(self, book_id):
        return self.session.query(BooksDBModel).filter(BooksDBModel.id == book_id).one_or_none()

    @check_session()
    def get_book_by_partial_name(self, name):
        return self.session.query(BooksDBModel).filter(BooksDBModel.name.ilike(f'%{name}%')).all()

    @check_session()
    def get_books_by_author(self, author):
        return self.session.query(BooksDBModel).filter(BooksDBModel.author == author).all()

    @check_session()
    def get_book_by_author_and_name(self, author, name):
        return self.session.query(BooksDBModel) \
            .filter(BooksDBModel.author == author,
                    BooksDBModel.name == name).one_or_none()

    @check_session()
    def get_books_by_partial_author_name(self, partial_name):
        return self.session.query(BooksDBModel) \
            .filter(BooksDBModel.author.ilike(f'%{partial_name}%')).all()

    @check_session()
    def get_reserved_books(self):
        result = self.session.query(UsersDBModel, BooksDBModel) \
            .join(ReservationsDBModel, UsersDBModel.id == ReservationsDBModel.user_id) \
            .join(BooksDBModel, ReservationsDBModel.book_id == BooksDBModel.id)\
            .all()
        return result

    @check_session()
    def get_full_reserved_books_info(self):
        result = self.session.query(UsersDBModel, BooksDBModel, ReservationsDBModel) \
            .join(ReservationsDBModel, UsersDBModel.id == ReservationsDBModel.user_id) \
            .join(BooksDBModel, ReservationsDBModel.book_id == BooksDBModel.id)\
            .order_by(UsersDBModel.first_name).all()
        return result

    @check_session()
    def get_reserved_book_by_user_id_and_book_id(self, user_id, book_id):
        result = self.session.query(UsersDBModel, BooksDBModel, ReservationsDBModel) \
            .join(ReservationsDBModel, UsersDBModel.id == ReservationsDBModel.user_id)\
            .join(BooksDBModel, ReservationsDBModel.book_id == BooksDBModel.id)\
            .filter(UsersDBModel.id == user_id)\
            .filter(BooksDBModel.id == book_id).one_or_none()
        return result

    @check_session()
    def update_user_by_values(self, user_id, user):
        updated_rows = self.session.query(UsersDBModel).filter(UsersDBModel.id == user_id).update(
            {"first_name": user.first_name,
             "last_name": user.last_name,
             "email": user.email})
        return updated_rows

    @check_session()
    def update_user(self, user_id, user):
        updated_rows = self.session.query(UsersDBModel).filter(UsersDBModel.id == user_id).update(user.serialize())
        return updated_rows

    @check_session()
    def update_book(self, book_id, book):
        updated_rows = self.session.query(BooksDBModel).filter(BooksDBModel.id == book_id).update(book.serialize())
        return updated_rows

    @check_session()
    def update_reservation(self, reservation):
        updated_rows = self.session.query(ReservationsDBModel) \
            .filter(ReservationsDBModel.book_id == reservation.book_id) \
            .filter(ReservationsDBModel.user_id == reservation.user_id).update(reservation.serialize())
        return updated_rows

    @check_session()
    def update_reservation_for_user(self, user_id, reservation):
        updated_rows = self.session.query(ReservationsDBModel) \
            .filter(ReservationsDBModel.user_id == user_id) \
            .update({"reservation_date": reservation.reservation_date,
                     "reservation_expiration_date": reservation.reservation_expiration_date})
        return updated_rows

    @check_session()
    def get_reserved_books_by_user_id(self, user_id):
        result = self.session.query(UsersDBModel, BooksDBModel, ReservationsDBModel) \
            .join(ReservationsDBModel, UsersDBModel.id == ReservationsDBModel.user_id) \
            .join(BooksDBModel, ReservationsDBModel.book_id == BooksDBModel.id) \
            .filter(UsersDBModel.id == user_id).all()
        return result

    @check_session()
    def get_reservation_by_book_id(self, book_id):
        result = self.session.query(UsersDBModel, BooksDBModel, ReservationsDBModel) \
            .join(ReservationsDBModel, UsersDBModel.id == ReservationsDBModel.user_id) \
            .join(BooksDBModel, ReservationsDBModel.book_id == BooksDBModel.id) \
            .filter(BooksDBModel.id == book_id).all()
        return result

    @check_session()
    def delete_user_by_id(self, user_id):
        deleted_rows = self.session.query(UsersDBModel).filter(UsersDBModel.id == user_id).delete()
        return deleted_rows

    @check_session()
    def delete_book_by_id(self, book_id):
        deleted_rows = self.session.query(BooksDBModel).filter(BooksDBModel.id == book_id).delete()
        return deleted_rows

    @check_session()
    def delete_reservation_by_user_and_book_id(self, user_id, book_id):
        deleted_rows = self.session.query(ReservationsDBModel)\
            .filter(ReservationsDBModel.book_id == book_id)\
            .filter(ReservationsDBModel.user_id == user_id).delete()
        return deleted_rows

    @check_session()
    def delete_reservation_by_user(self, user_id):
        deleted_rows = self.session.query(ReservationsDBModel)\
            .filter(ReservationsDBModel.user_id == user_id).delete()
        return deleted_rows

    @check_session()
    def delete_reservation_by_book(self, book_id):
        deleted_rows = self.session.query(ReservationsDBModel) \
            .filter(ReservationsDBModel.book_id == book_id).delete()
        return deleted_rows

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



