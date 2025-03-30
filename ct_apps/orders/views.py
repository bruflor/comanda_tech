from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class SaleOrdersView(View):
    def get(self, request):
        context = {}
        return render(request, 'orders/index.html', context)


class SaleOrdersDetailView(View):
    def get(self, request, id):
        context = {
            "id": "00123",
            "user": "Wes",
            "purchased_items": [
                {
                    "id": "123456",
                    "amount": 3,
                    "name": 'Feijoada',
                    "price": 10.00
                },
                {
                    "id": "234567",
                    "amount": 5,
                    "name": 'Cocola',
                    "price": 1.00
                },
                {
                    "id": "34567",
                    "amount": 3,
                    "name": 'Sagu',
                    "price": 1.50
                },
                {
                    "id": "4567",
                    "amount": 3,
                    "name": 'Canjica',
                    "price": 0.80
                }
            ],
            "retrieved_items": [
                {
                    "id": "#4567",
                    "name": 'Canjica',
                    "timestamp": "date-time"
                }
            ]
        }
        return render(request, 'orders/roles/consumer.html', context)
