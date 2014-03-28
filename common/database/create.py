# -*- coding: utf-8 -*-
from __future__ import absolute_import

from common.flask import app
from . import models

def create_all():
    models.model_base.ModelBase.metadata.create_all(app.db)

