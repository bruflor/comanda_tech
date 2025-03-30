from django.urls import path
from . import views

app_name="orders"

urlpatterns = [
    path('', views.SaleOrdersView.as_view(), name='list'),
    path('<str:id>/', views.SaleOrdersDetailView.as_view(), name='detail'),
    path('<str:id>/<is_editing>', views.SaleOrdersDetailEditingView.as_view(), name='detail_edit'),
]