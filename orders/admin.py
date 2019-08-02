""" inventory admin """

from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
