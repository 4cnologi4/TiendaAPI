from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model


# class Usuario(AbstractUser):
#     pass


class Client(models.Model):
    name = models.CharField(max_length=20)
    app = models.CharField(max_length=30)
    apm = models.CharField(max_length=30)


class Category(models.Model):
    description = models.CharField(max_length=100, null=True, blank=True)
    subcategory = models.CharField(max_length=40, null=True)


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=55)
    value = models.FloatField()
    discount_value = models.FloatField(null=True, blank=True)
    stock = models.IntegerField()


class Sales(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False, blank=False)
