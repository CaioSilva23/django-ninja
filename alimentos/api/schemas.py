from ninja import Schema, ModelSchema
from typing import List, Dict
from ..models import Alimento as ModelAlimento

class Alimento(ModelSchema):
    class Config:
        model = ModelAlimento
        model_fields = ['nome', 'qtde']
        # OU USAR model_exclude = ['id']
