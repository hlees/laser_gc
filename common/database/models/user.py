# -*- coding: utf-8 -*-
from __future__ import absolute_import

from sqlalchemy import Column, Integer, Text, ForeignKey, Numeric, DateTime, Boolean
from sqlalchemy.orm import relationship
from .model_base import ModelBase, DictionaryConvertable
from .json_type import JsonType


class User(ModelBase, DictionaryConvertable):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False)
    device_id = Column(Text, nullable=False)
    
    social_token = Column(Text, nullable=True)

    stage_open = Column(Integer, nullable=False)
    stage_clear = Column(Integer, nullable=False)

    hint = Column(Integer, nullable=False)
