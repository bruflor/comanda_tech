from django.contrib import admin

from ct_apps.orders.models import OrderSale, OrderItem, Product


# Register your models here.
@admin.register(OrderSale, OrderItem, Product)
class OrderSaleAdmin(admin.ModelAdmin):
    pass


# @admin.register(OrderItem)
# class OrderItem(admin.AdminSite):
#     pass


# @admin.register(Product)
# class ProductAdmin(admin.AdminSite):
#     pass
