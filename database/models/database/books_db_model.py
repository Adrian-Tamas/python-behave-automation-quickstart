import json

from sqlalchemy import Column, String

from database import Base
from database.models.database.sqlalchemy_serializer import SQLAlchemySerializer


class BooksDBModel(Base, SQLAlchemySerializer):
    __tablename__ = f'books'

    id = Column(String, primary_key=True)
    name = Column(String)
    author = Column(String)
    description = Column(String)
    cover = Column(String)

    def __init__(self, **fields):
        self.id = fields.get("id", None)
        self.name = fields["name"]
        self.author = fields["author"]
        self.description = fields.get("description", None)
        self.cover = fields.get("cover", None)

    def __repr__(self):
        return f"{json.dumps(self.serialize())}"
