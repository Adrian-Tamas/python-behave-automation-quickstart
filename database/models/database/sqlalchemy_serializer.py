from sqlalchemy.inspection import inspect


class SQLAlchemySerializer(object):
    """
    Class defined to serialize query results to Python dicts. Make sure any model you define extends Base and this class
    """

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
