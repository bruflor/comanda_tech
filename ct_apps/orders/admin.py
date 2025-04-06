from django.contrib import admin

from ct_apps.orders.models import OrderSale, OrderItem, Product, Transaction


# Register your models here.
@admin.register(OrderSale)
class OrderSaleAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ['reference', 'consumer' ]
    list_filter = ['reference', 'consumer']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ['name', 'price', 'stock_unity']
    list_filter = ['name', 'price', 'stock_unity']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ['order', 'item', 'status', 'updated_at']
    list_filter = ['item', 'order', 'status', 'updated_at']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ['amount', 'payment_method', 'order', 'created_at','updated_at']
    list_filter = ['payment_method', 'order']
