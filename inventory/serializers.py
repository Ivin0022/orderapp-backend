from rest_framework import serializers

from .models import Inventory, Category


class CategorySerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='item'
    )

    class Meta:
        model = Category
        fields = ['url', 'items', 'itemType']


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ['url', 'item', 'itemType']
