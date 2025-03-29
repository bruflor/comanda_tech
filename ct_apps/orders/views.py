from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "user": {
            "name": "Wes",
            "type":"consumer"
        },
        "sale_order": {
            "id": '00123',
            "items": [
                {
                    "id": "#123456",
                    "amount": 3,
                    "name": 'Feijoada',
                    "price": 10.00
                },
                {
                    "id": "#234567",
                    "amount": 5,
                    "name": 'Cocola',
                    "price": 1.00
                },
                {
                    "id": "#34567",
                    "amount": 3,
                    "name": 'Sagu',
                    "price": 1.50
                },
                {
                    "id": "#4567",
                    "amount": 3,
                    "name": 'Canjica',
                    "price": 0.80
                }
            ]
        }

    }
    return render(request, 'orders/index.html', context)
