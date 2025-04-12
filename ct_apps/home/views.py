# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from ct_apps.orders.models import OrderSale


class HomeView(View):
    def get(self, request, order_id=None):
        context = {}

        if request.GET.get('search_order_id'):
            order_id = request.GET.get('search_order_id')
            return HttpResponseRedirect(f"/{order_id}")

        if order_id:
            try:
                order = OrderSale.objects.get(reference__iexact=order_id)
                context["order"] = order
            except ObjectDoesNotExist:
                pass

        return render(request, "home/index.html", context=context)
