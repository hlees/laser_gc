from sqlalchemy.ext.declarative import declarative_base

ModelBase = declarative_base()
class DictionaryConvertable():
    def to_dict(self):
        d = {}
	for column in self.__table__.columns:
	    d[column.name] = getattr(self, column.name)

	return d
