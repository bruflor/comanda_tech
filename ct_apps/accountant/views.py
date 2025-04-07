from django.shortcuts import render
from django.views import View

from ct_apps.orders.models import Product, Transaction


# Create your views here.
class AccountantDashBoardView(View):
    def get(self, request):
        product = Product.objects.all().exclude(is_internal=True)
        transaction = Transaction.objects.all()

        context = {
            'product': product,
            'transaction': transaction
        }

        return render(request, "accountant/index.html", context=context)
