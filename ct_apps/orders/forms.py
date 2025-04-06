from django import forms

from ct_apps.orders.models import Product


class ProductForm(forms.Form):
    products_choice = [(p.id, p.name, p.price, p.stock_unity) for p in
                       Product.objects.filter(stock_unity__gt=0).exclude(name__istartswith="internal").order_by('name')]

    Item = forms.ChoiceField(choices=products_choice)
