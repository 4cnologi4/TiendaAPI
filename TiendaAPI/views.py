from django.http import JsonResponse
from TiendaAPI.models import Products


def getProductos(self):
    productos = Products.objects.all()
    data = list(
        productos.values("pid", "name", "value", "discount_value", "stock"))
    return JsonResponse({ "Productos": data}, safe=False)