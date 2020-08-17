from django.http import JsonResponse
from TiendaAPI.models import Products
from rest_framework import viewsets
from TiendaAPI.serializers import ProductsSerializer


def getProductos(self):
    productos = Products.objects.all()
    data = list(
        productos.values("id", "name", "value", "discount_value", "stock"))
    return JsonResponse({ "Productos": data}, safe=False)


class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
