""" views for inventroy app """

from rest_framework import viewsets
from django.views.generic import ListView
from .models import Inventory, Category
from .serializers import InventorySerializer, CategorySerializer


class InventoryList(ListView):
    """ list view of Inventory """
    model = Inventory


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
