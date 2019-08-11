""" views for inventroy app """

from rest_framework import viewsets
from django.views.generic import ListView
from .models import Inventory, Category
from .serializers import InventorySerializer, CategorySerializer, InventoryListSerializer


class InventoryList(ListView):
    """ list view of Inventory """
    model = Inventory


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return InventoryListSerializer
        return super().get_serializer_class()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
