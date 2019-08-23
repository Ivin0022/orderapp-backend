""" doc for modles in patients """

from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Patient(models.Model):
    """ docstring for patients """
    name = models.CharField(max_length=50)
    age = models.IntegerField('Age')
    case_no = models.CharField(max_length=6, unique=True)
    next_of_kin = models.CharField(max_length=50, null=True)
    date = models.DateField('date', default=timezone.now())
    occupation = models.CharField(max_length=50, null=True)
    mobile = PhoneNumberField()
    address = models.TextField(default='')
    email = models.EmailField(null=True)

    def __str__(self):
        return f'{self.name} ({self.age})'
