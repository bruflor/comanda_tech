from django.urls import path
from . import views

app_name="orders"

urlpatterns = [
    path('', views.SaleOrdersView.as_view(), name='list'),
    path("add/", views.SaleOrderAddView.as_view(), name='detail_edit_sales_add'),
    path('<str:reference>/', views.SaleOrdersDetailView.as_view(), name='detail'),
    path('<str:reference>/<is_editing>', views.SaleOrdersDetailEditingView.as_view(), name='detail_edit'),
    path('<str:reference>/<is_editing>/<is_sales>/', views.SaleOrdersDetailEditingView.as_view(), name='detail_edit_sales'),
]
