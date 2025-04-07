import sys

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from ct_apps.orders.models import OrderSale, OrderItem, Product, Transaction

if 'makemigrations' not in sys.argv and 'migrate' not in sys.argv:
    from ct_apps.orders.forms import ProductForm


# Create your views here.
# List view - staff and sales
class SaleOrdersView(View):
    def get(self, request):
        order_sales = OrderSale.objects.exclude(reference__startswith='internal_')

        # for param in request.GET.items():
        #     print(param)

        context = {
            "sale_order": [so for so in order_sales]
        }

        search_order_ref = request.GET.get('search_order_id', None)

        if search_order_ref:
            print('here searching')
            context['sale_order'] = order_sales.filter(reference__contains=search_order_ref)

        print(context, 'context')

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
    def get(self, request, reference, is_editing, is_sales=False, *args, **kwargs):

        order_sale = OrderSale.objects.get(reference=reference)
        purchased_item = order_sale.purchased_item.all

        product_form = ProductForm()

        product_choice = [(p.id, p.name, p.price, p.stock_unity) for p in
                          Product.objects.filter(stock_unity__gt=0).exclude(is_internal=True).order_by('name')]

        product_form.fields['Item'].choices = product_choice

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
            "product_form": product_form,
            "is_sales": is_sales
        }

        if is_sales:
            return render(request, "orders/sales_order/edit/sales_editing.html", context)
        return render(request, 'orders/sales_order/edit/staff_editing.html', context)

    def post(self, request, reference, is_editing, is_sales=None):
        order_sale = OrderSale.objects.get(reference=reference)
        purchased_item = order_sale.purchased_item.all()

        product_form = ProductForm()

        product_choice = [(p.id, p.name, p.price, p.stock_unity) for p in
                          Product.objects.filter(stock_unity__gt=0).exclude(is_internal=True).order_by('name')]

        product_form.fields['Item'].choices = product_choice

        for k, v in request.POST.items():
            if k != "csrfmiddlewaretoken":
                # reach just when adding new items 
                if k == 'item_id' and not k.startswith('status'):
                    order_item = purchased_item.create(
                        item=Product.objects.get(pk=v), order=order_sale, amount=1)
                    order_item.save()

                elif k != "paid" and k != 'consumer-name' and not k.startswith('status') and k != 'payment-method':
                    order_item = purchased_item.get(pk=k)
                    order_item.amount = v
                    order_item.status = 'paid'
                    order_item.save()

                elif k == 'consumer-name':
                    order_sale.consumer = v
                    order_sale.save()

                elif k.startswith('status'):
                    id = k.split('_')[1]
                    order_item = purchased_item.get(pk=id)
                    order_item.status = v
                    order_item.save()
                else:
                    for item in purchased_item:
                        if request.POST.get(f'status_{item.id}'):
                            if item.status == 'to_pay':
                                item.status = 'paid'

                                product = Product.objects.get(pk=item.item.id)
                                product.stock_unity -= 1
                                product.save()

                                item.save()

                            if item.status == 'to_remove':
                                item.delete()
                    if k != 'payment-method':
                        payment_method = request.POST.get('payment-method')
                        Transaction.objects.create(order=order_sale, amount=v,
                                                   payment_method=payment_method).save()

                    is_sales = False

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
            "product_form": product_form,
            "is_sales": is_sales
        }

        if is_sales:
            return render(request, "orders/sales_order/edit/sales_editing.html", context)

        return HttpResponseRedirect(f'/orders/{reference}/True')


# Sales/admin view
class SaleOrderAddView(View):
    def get(self, request, reference, is_editing, is_sales=None, *args, **kwargs):
        order_sale = OrderSale.objects.get(reference=reference)
        purchased_item = order_sale.purchased_item.all

        product_form = ProductForm()

        product_choice = [(p.id, p.name, p.price, p.stock_unity) for p in
                          Product.objects.filter(stock_unity__gt=0).exclude(is_internal=True).order_by('name')]

        product_form.fields['Item'].choices = product_choice

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

        product_choice = [(p.id, p.name, p.price, p.stock_unity) for p in
                          Product.objects.filter(stock_unity__gt=0).exclude(is_internal=True).order_by('name')]

        product_form.fields['Item'].choices = product_choice

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
