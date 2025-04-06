from django.contrib import admin

from ct_apps.orders.models import OrderSale, OrderItem, Product


# Register your models here.
@admin.register(OrderSale)
class OrderSaleAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ['name', 'price', 'stock_unity']
    list_filter = ['name', 'price', 'stock_unity']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ['order', 'item', 'status']
    list_filter = ['item', 'order', 'status']
