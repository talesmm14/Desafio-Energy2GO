from django.urls import path

from apps.sales import views

urlpatterns = [
    path('transaction/', views.transactions, name='transactions'),
    path('transaction/<int:pk>/', views.transaction, name='transaction'),
    path('stations/<int:pk>/receive_payment/', views.receive_payment, name='receive_payment'),
]
