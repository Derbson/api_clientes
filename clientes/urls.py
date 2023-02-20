from django.urls import path, include
from .views import ClientesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes',ClientesViewSet, basename='Clientes')

urlpatterns = [
    path('', include(router.urls)),
]


