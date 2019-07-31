""" models for orders """

from django.db import models

from patients.models import Patient
from inventory.models import Inventory


class Order(models.Model):
    """ docstring for the class """

    STATUS_CHOICES = (
        ('p', 'placed'),
        ('s', 'seen'),
        ('f', 'fulfiled'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time_of_placement = models.DateTimeField('order placed')
    time_of_fulfilment = models.DateTimeField('order fulfiled')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    items = models.ManyToManyField(Inventory)
