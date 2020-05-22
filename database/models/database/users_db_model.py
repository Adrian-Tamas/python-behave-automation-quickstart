import json
from sqlalchemy import Column, String

from database import Base
from database.models.database.sqlalchemy_serializer import SQLAlchemySerializer


class UsersDBModel(Base, SQLAlchemySerializer):
    __tablename__ = f'users'

    id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)

    def __init__(self, **fields):
        self.id = fields.get("id", None)
        self.first_name = fields["first_name"]
        self.last_name = fields["last_name"]
        self.email = fields["email"]

    def __repr__(self):
        return f"{json.dumps(self.serialize())}"
