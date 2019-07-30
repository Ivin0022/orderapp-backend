""" views for inventroy app """

from django.views.generic import ListView
from .models import Inventory


class InventoryList(ListView):
    """ list view of Inventory """
    model = Inventory
