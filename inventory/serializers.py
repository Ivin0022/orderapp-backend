from rest_framework import serializers

from .models import Inventory, Category


class CategorySerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Category
        fields = ['url', 'items', 'name']


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ['url', 'name', 'category']


class InventoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ['url', 'name', 'category']
        depth = 1
