from django import forms

from ct_apps.orders.models import Product


class ProductForm(forms.Form):
    products_choice = [(p.id, p.name, p.price, p.stock_unity) for p in Product.objects.all().order_by('name')]
    
    Item = forms.ChoiceField(choices=products_choice)
