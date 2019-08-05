from rest_framework import serializers

from .models import Inventory, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'itemType']


class InventorySerializer(serializers.ModelSerializer):
    itemType = CategorySerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = ['url', 'item', 'itemType']
