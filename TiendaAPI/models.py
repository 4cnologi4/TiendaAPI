from django.db import models
from django.db.models import Model


class Products(models.Model):
    pid = models.CharField(max_length=10)
    name = models.CharField(max_length=55)
    value = models.FloatField()
    discount_value = models.FloatField(null=True, blank=True)
    stock = models.IntegerField()