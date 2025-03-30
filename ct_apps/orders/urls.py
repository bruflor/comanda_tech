from django.urls import path
from . import views

urlpatterns = [
    path('<str:id>/', views.SaleOrdersDetailView.as_view()),
]