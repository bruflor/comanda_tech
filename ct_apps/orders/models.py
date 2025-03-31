from django.db import models


# Create your models here.
class SaleOrder(models.Model):
    consumer = models.CharField(max_length=200, default="", null=True, blank=True)
    purchased_items = model


class AppUser(models.Model):
    pass


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(null=False, blank=False, default=0.0)
    stock_unity = models.IntegerField(null=False, blank=False, default=1)
    cost_per_unity = models.FloatField(null=True, blank=True)
