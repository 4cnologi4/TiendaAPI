from rest_framework import serializers
from TiendaAPI.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'category', 'name', 'value', 'stock']
