from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import View

from ct_apps.orders.forms import ProductForm
from ct_apps.orders.models import OrderSale, OrderItem, Product


# Create your views here.
# List view - staff and sales
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


# Consumer view
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


# Staff view
class SaleOrdersDetailEditingView(View):
    def get(self, request, reference, is_editing, is_sales=None, *args, **kwargs):

        order_sale = OrderSale.objects.get(reference=reference)
        purchased_item = order_sale.purchased_item.all

        product_form = ProductForm()

        context = {
            "order_sale": order_sale,
            "purchased_items": purchased_item,
            "retrieved_items": [
                {
                    "id": "#4567",
                    "name": 'Canjica',
                    "timestamp": "date-time"
                }
            ],
            "product_form": product_form
        }

        if is_sales:
            return render(request, "orders/sales_order/edit/sales_editing.html", context)
        return render(request, 'orders/sales_order/edit/staff_editing.html', context)

    def post(self, request, reference, is_editing, is_sales=None):
        order_sale = OrderSale.objects.get(reference=reference)
        purchased_item = order_sale.purchased_item.all()

        product_form = ProductForm()

        for k, v in request.POST.items():
            print(k, v)
            if k != "csrfmiddlewaretoken":
                # reach just when adding new items 
                if k == 'item_id':
                    print('item_id')
                    try:
                        order_item = purchased_item.get(item_id__exact=v)
                        order_item.amount += 1
                        order_item.save()
                    except ObjectDoesNotExist:
                        order_item = purchased_item.create(
                            item=Product.objects.get(pk=v), order=order_sale, amount=5)
                        order_item.save()

                # pass through here when changing the amount of items  
                else:
                    if k != "paid" and k != 'consumer_name':
                        order_item = purchased_item.get(pk=k)
                        order_item.amount = v
                        order_item.save()
                    elif k == 'consumer_name':
                        # todo: updating the name
                        print('updating the name')
                    else:
                        # TODO: adding payment to the cashflow
                        print('adding payment to the cashflow')

        context = {
            "order_sale": order_sale,
            "purchased_items": purchased_item.all(),
            "retrieved_items": [
                {
                    "id": "#4567",
                    "name": 'Canjica',
                    "timestamp": "date-time"
                }
            ],
            "product_form": product_form
        }
        return render(request, 'orders/sales_order/edit/staff_editing.html', context)


# Sales/admin view
class SaleOrderAddView(View):
    def get(self, request, reference, is_editing, is_sales=None, *args, **kwargs):
        order_sale = OrderSale.objects.get(reference=reference)
        purchased_item = order_sale.purchased_item.all

        product_form = ProductForm()

        context = {
            "order_sale": order_sale,
            "purchased_items": purchased_item,
            "retrieved_items": [
                {
                    "id": "#4567",
                    "name": 'Canjica',
                    "timestamp": "date-time"
                }
            ],
            "product_form": product_form
        }

        return render(request, "orders/sales_order/edit/sales_editing.html", context)

    def post(self, request):
        reference = request.POST.get("reference", None)
        item_id = request.POST.get("item_id", None)

        order_sale = OrderSale.objects.get(reference=reference)
        purchased_item = order_sale.purchased_item

        order_item = OrderItem(item_id=item_id, order=order_sale, amount=1)
        order_item.save()

        product_form = ProductForm()

        context = {
            "order_sale": order_sale,
            "purchased_items": purchased_item.all(),
            "retrieved_items": [
                {
                    "id": "#4567",
                    "name": 'Canjica',
                    "timestamp": "date-time"
                }
            ],
            "product_form": product_form
        }

        return render(request, "orders/sales_order/edit/sales_editing.html", context)
