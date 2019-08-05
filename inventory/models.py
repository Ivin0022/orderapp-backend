""" doc for inventory models """

from django.db import models


class Category(models.Model):
    """ docstring for Category """

    itemType = models.CharField(max_length=20)

    def __str__(self):
        return self.itemType

    class Meta:
        verbose_name_plural = "Categories"


class Inventory(models.Model):
    """ docstring for Inventory """

    itemType = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    item = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.item} ({self.itemType})'

    class Meta:
        verbose_name_plural = "Inventories"
