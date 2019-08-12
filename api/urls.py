from django.urls import path, include
from rest_framework import routers

from patients.views import PatientViewSet
from inventory.views import InventoryViewSet, CategoryViewSet
from orders.views import OrderViewSet

router = routers.DefaultRouter()
router.register('order', OrderViewSet)
router.register('patient', PatientViewSet)
router.register('inventory', InventoryViewSet)
router.register('category', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls))
]
