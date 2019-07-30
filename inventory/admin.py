""" inventory admin """

from django.contrib import admin
from .models import Inventory, Category

admin.site.register(Inventory)
admin.site.register(Category)
