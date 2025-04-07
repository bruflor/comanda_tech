from django.urls import path
from . import views

app_name = "accountant"

urlpatterns = [
    path('', views.AccountantDashBoardView.as_view(), name='index'),
    path('download-csv-products', views.download_csv_products, name='download_csv_product'),
    path('download-csv-transactions', views.download_csv_transactions, name='download_csv_transaction'),
]
