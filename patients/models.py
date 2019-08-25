""" doc for modles in patients """

from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Patient(models.Model):
    """ docstring for patients """
    name = models.CharField(max_length=50)
    age = models.IntegerField('Age')
    case_no = models.CharField(max_length=6, unique=True)
    next_of_kin = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField('date', default=timezone.now())
    occupation = models.CharField(max_length=50, null=True, blank=True)
    mobile = PhoneNumberField(null=True, blank=True)
    address = models.TextField(default='', blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.age})'
