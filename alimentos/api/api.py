from ninja import Router
from django.http import JsonResponse
from .schemas import Alimento
from ..models import Alimento as ModelAlimento
from django.shortcuts import get_object_or_404

alimentos_router = Router()

# alimentos = [
#     {'Nome': 'Banana', 'Qtd': 5, 'id': 1},
#     {'Nome': 'Carne', 'Qtd': 9, 'id': 2},
#     {'Nome': 'Pera', 'Qtd': 15, 'id': 3}
# ]


# PARAMETROS DE URL 
# @alimentos_router.get('/{int:id}')
# def get_alimento(request, id: int):
#     alimento = list(filter(lambda x: x['id'] == id, alimentos))
#     if len(alimento) > 0:
#         return JsonResponse(alimento[0])
#     return JsonResponse({'Error': 'Alimento não encontrado'})


# PARAMETROS DE CONSULTA
# @alimentos_router.get('/{int:id}/')
# def get_alimento(request, id: int, preco_min: str = 10):
#     return JsonResponse({'id': id, 'preco_min': preco_min})


# @alimentos_router.post('/')
# def get_alimento(request, alimento: Alimento):
#     print(alimento.nome)
#     print(alimento.qtde)
#     print(alimento.variedades)
#     return JsonResponse({'id': 1})


    
@alimentos_router.get('/one/{id}/', response=Alimento)
def get_alimento(request, id: int) -> Alimento:
    alimento = get_object_or_404(ModelAlimento, id=id)
    return alimento


@alimentos_router.get('/all/', response=Alimento)
def get_alimentos(request) -> Alimento:
    alimentos = ModelAlimento.objects.all().values()
    print(alimentos)
    return JsonResponse({'alimentos': list(alimentos)})


#post
#@alimentos_router.post('/')
#def post_alimento(request, alimento: Alimento):
#    a = ModelAlimento(nome=alimento.nome, qtde= alimento.qtde)
#    a.save()
#    return alimento