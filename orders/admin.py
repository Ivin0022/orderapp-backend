""" inventory admin """

from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('patient', 'time_of_placement',
                    'time_of_fulfillment', 'status')

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
