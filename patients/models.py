""" doc for modles in patients """

from django.db import models


class Patient(models.Model):
    """ docstring for patients """
    name = models.CharField(max_length=50)
    age = models.IntegerField('Age')
    case_no = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f'{self.name} ({self.age})'
