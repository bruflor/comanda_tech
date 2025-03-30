from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class SaleOrdersView(View):
    def get(self, request):

        for param in request.GET.items():
            print(param)

        context = {
            "sales_orders": [
                {
                    "id": "00123",
                    "user": "Wes",
                    "status": 1,
                    "has_pending_items": 1
                },
                {
                    "id": "00124",
                    "user": "Bru",
                    "status": 1,
                    "has_pending_items": 0
                }
            ]
        }

        if request.GET.get('search_order_id', None):
            print('here')
            context['sales_orders'] = [context['sales_orders'][0]]

        print(context)

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
                    "amount": 352,
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
        return render(request, 'orders/sales_order/index.html', context)


class SaleOrdersDetailEditingView(View):
    def get(self, request, id, is_editing, *args, **kwargs):
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
                    "amount": 365,
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

        return render(request, 'orders/sales_order/editing.html', context)

    def post(self, request, id, is_editing ):
        print(request.POST.get("body"))
        return HttpResponse('success')

