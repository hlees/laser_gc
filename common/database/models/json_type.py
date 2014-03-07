import json
import sqlalchemy.types as types

class JsonType(types.TypeDecorator):

    impl = types.String

    def process_bind_param(self, value, dialect):
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        return json.loads(value)

    def copy(self):
        return JsonType(self.impl.length)

