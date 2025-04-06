from django import forms

from ct_apps.orders.models import Product


class ProductForm(forms.Form):
    Item = forms.ChoiceField()
