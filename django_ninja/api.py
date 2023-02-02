from ninja import NinjaAPI
from alimentos.api.api import alimentos_router
from pacientes.api.api import pacientes_router


api = NinjaAPI()

api.add_router('/alimentos', alimentos_router)
api.add_router('/pacientes', pacientes_router)