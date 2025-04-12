# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from ct_apps.orders.models import OrderSale, Product


class HomeView(View):
    def get(self, request, order_id=None):

        products = Product.objects.filter(sold_unity__lt=F("initial_stock")).exclude(is_internal=True).order_by(
            'name')

        context = {"products": products}

        if request.GET.get('search_order_id'):
            order_id = request.GET.get('search_order_id')
            return HttpResponseRedirect(f"/{order_id}")

        if order_id:
            try:
                order = OrderSale.objects.get(reference__iexact=order_id)
                context["order"] = order
                purchased_item = order.purchased_item.all

                context = {
                    "order_sale": order,
                    "purchased_items": purchased_item,

                }

            except ObjectDoesNotExist:
                pass

        return render(request, "home/index.html", context=context)
