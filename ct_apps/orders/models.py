from django.db import models


# Create your models here.
class OrderSale(models.Model):
    consumer = models.CharField(max_length=200, default="", null=True, blank=True)
    reference = models.CharField(max_length=200, default="")
    
    def __str__(self):
        return f"{self.consumer}"


class OrderItem(models.Model):
    item = models.ForeignKey("Product", on_delete=models.CASCADE)
    order = models.ForeignKey("OrderSale", on_delete=models.CASCADE, related_name='purchased_item')
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.order.consumer} : {self.item.name} "


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(null=False, blank=False, default=0.0)
    stock_unity = models.IntegerField(null=False, blank=False, default=1)
    cost_per_unity = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"
