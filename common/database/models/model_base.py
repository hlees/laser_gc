from sqlalchemy.ext.declarative import delcarative_base

ModelBase = declarative_base()
class DictionaryConvertable():
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


