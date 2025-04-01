from django.shortcuts import render
from django.views import View

from ct_apps.orders.models import OrderSale


# Create your views here.
class SaleOrdersView(View):
    def get(self, request):

        sale_order = OrderSale.objects.all()

        for param in request.GET.items():
            print(param)

        context = {
            "sale_order": [so for so in sale_order]
        }

        if request.GET.get('search_order_id', None):
            print('here')
            context['sales_orders'] = [context['sales_orders'][0]]

        print(context)

        return render(request, 'orders/index.html', context)


class SaleOrdersDetailView(View):
    def get(self, request, reference):
        order_sale = OrderSale.objects.get(reference=reference)
        purchased_item = order_sale.purchased_item.all



        context = {
            "order_sale": order_sale,
            "purchased_items": purchased_item,
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
    def get(self, request, reference, is_editing, *args, **kwargs):

        order_sale = OrderSale.objects.get(reference=reference)
        purchased_item = order_sale.purchased_item.all



        context = {
            "order_sale": order_sale,
            "purchased_items": purchased_item,
            "retrieved_items": [
                {
                    "id": "#4567",
                    "name": 'Canjica',
                    "timestamp": "date-time"
                }
            ]
        }

        return render(request, 'orders/sales_order/editing.html', context)

    def post(self, request, reference, is_editing):
        order_sale = OrderSale.objects.get(reference=reference)
        purchased_item = order_sale.purchased_item
        
        for k,v in request.POST.items():
            # print(k,v)
            if k != "csrfmiddlewaretoken":
                item = purchased_item.get(item_id=k)
                item.amount=v
                item.save()



        context = {
            "order_sale": order_sale,
            "purchased_items": purchased_item.all(),
            "retrieved_items": [
                {
                    "id": "#4567",
                    "name": 'Canjica',
                    "timestamp": "date-time"
                }
            ]
        }

        # pi = []
        # for item in request.POST.items():
        #     item_to_append = {}
        #     for x in context['purchased_items']:
        #         x[item[0]] = item[1]
        #         item_to_append = x
        # 
        #     pi.append(item_to_append)
        # 
        # context['purchased_items'] = pi

        return render(request, 'orders/sales_order/editing.html', context)
