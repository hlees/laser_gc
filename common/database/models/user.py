from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime, Boolean
from sqlalchemy.orm import relationship
from .model_base import ModelBase, DictionaryConvertable
from .json_type import JsonType


class User(ModelBase, DictionaryConvertable):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False)
    device_id = Column(String(100), nullable=False)
    
    social_token = Column(String, nullable=True)

