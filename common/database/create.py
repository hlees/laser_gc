from .session import engine
from . import models

models.model_base.ModelBase.metadata.create_all(engine)

