from rest_framework import serializers

from .models import Inventory, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['url', 'items', 'itemType']
        depth = 1


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ['url', 'item', 'itemType']
        depth = 1
