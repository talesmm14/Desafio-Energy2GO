from django.urls import path, include

urlpatterns = [
    path('hardware/', include('apps.hardware.urls')),
    path('sales/', include('apps.sales.urls')),
]
