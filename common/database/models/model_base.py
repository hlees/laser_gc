from sqlalchemy.ext.declarative import declarative_base
from common.flask import app

ModelBase = declarative_base()
ModelBase.query = app.db.session.query_property()

class DictionaryConvertable():
    def to_dict(self):
        d = {}
	for column in self.__table__.columns:
	    d[column.name] = getattr(self, column.name)

	return d
