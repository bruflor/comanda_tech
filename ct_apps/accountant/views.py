import csv
from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from ct_apps.orders.models import Product, Transaction


# Create your views here.
class AccountantDashBoardView(LoginRequiredMixin, View):
    def get(self, request):
        product = Product.objects.all().exclude(is_internal=True)
        total_collected = Transaction.objects.filter(amount__gt=0)

        partial_total = 0
        for t in total_collected:
            partial_total += t.amount

        context = {
            'product': product,
            'total_collected': partial_total
        }

        return render(request, "accountant/index.html", context=context)


def download_csv_products(request):
    # Create the HttpResponse object with CSV headers
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': f'attachment; filename="products_{datetime.now().strftime("%Y%m%d")}.csv"'},
    )

    # Create CSV writer
    writer = csv.writer(response)

    # Write CSV header
    writer.writerow(['Nome do produto', 'Preço', 'Estoque inicial', 'Quantidade vendida'])

    # Get queryset (customize this based on your needs)
    queryset = Product.objects.all().order_by("-sold_unity")

    # Write data rows
    for product in queryset:
        writer.writerow([
            product.name,
            product.price,
            product.initial_stock,
            product.sold_unity
        ])

    return response


def download_csv_transactions(request):
    # Create the HttpResponse object with CSV headers
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': f'attachment; filename="transactions_{datetime.now().strftime("%Y%m%d")}.csv"'},
    )

    # Create CSV writer
    writer = csv.writer(response)

    # Write CSV header
    writer.writerow(['Comanda (Reference)', 'Nome do consumidor', 'Valor gasto', 'Método de pagamento'])

    # Get queryset (customize this based on your needs)
    queryset = Transaction.objects.all().order_by("order__reference")

    # Write data rows
    for transaction in queryset:
        writer.writerow([
            transaction.order.reference,
            transaction.order.consumer,
            transaction.amount,
            transaction.payment_method
        ])

    return response
