from django.urls import path
from . import views

app_name = "accountant"

urlpatterns = [
    path('', views.AccountantDashBoardView.as_view(), name='index'),
    path('download-csv', views.download_csv, name='download_csv'),
]
