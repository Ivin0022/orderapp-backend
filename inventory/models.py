""" doc for inventory models """

from django.db import models


class Category(models.Model):
    """ docstring for Category """

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Inventory(models.Model):
    """ docstring for Inventory """

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name_plural = "Inventories"
