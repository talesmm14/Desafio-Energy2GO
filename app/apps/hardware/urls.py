from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.hardware import views

router = DefaultRouter()
router.register(r'stations', views.StationViewSet, basename='station')

urlpatterns = [
    path('', include(router.urls)),
]
