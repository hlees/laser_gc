from common.flask import app
from . import models

models.model_base.ModelBase.metadata.create_all(app.db)

