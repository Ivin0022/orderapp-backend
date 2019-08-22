""" doc for modles in patients """

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Patient(models.Model):
    """ docstring for patients """
    name = models.CharField(max_length=50)
    age = models.IntegerField('Age')
    case_no = models.CharField(max_length=6, unique=True)
    mobile = PhoneNumberField()

    def __str__(self):
        return f'{self.name} ({self.age})'
