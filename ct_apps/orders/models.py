from django.db import models


# Create your models here.
class OrderSale(models.Model):
    consumer = models.CharField(max_length=200, default="", null=True, blank=True)
    reference = models.CharField(max_length=200, default="")

    def __str__(self):
        return f"{self.reference} - {self.consumer}"


class OrderItem(models.Model):
    item = models.ForeignKey("Product", on_delete=models.CASCADE)
    order = models.ForeignKey("OrderSale", on_delete=models.CASCADE, related_name='purchased_item')
    amount = models.IntegerField(default=0)
    status = models.CharField(max_length=50, default='to_pay')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order.reference} : {self.item.name} "


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(null=False, blank=False, default=0.0)
    stock_unity = models.IntegerField(null=False, blank=False, default=1)
    cost_per_unity = models.FloatField(null=True, blank=True)
    is_internal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class Transaction(models.Model):
    order = models.ForeignKey("OrderSale", on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    payment_method = models.CharField(default="dinheiro", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
