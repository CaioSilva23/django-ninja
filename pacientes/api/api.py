from ninja import Router
from django.http import JsonResponse

pacientes_router = Router()

@pacientes_router.get('pacientes/')
def home(request):
    return JsonResponse({'teste': 'pacientes'})