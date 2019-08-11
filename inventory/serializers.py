from rest_framework import serializers

from .models import Inventory, Category


class TrackListingField(serializers.RelatedField):
    def to_representation(self, value):
        return f'v: {value}'


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


class InventoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ['url', 'item', 'itemType']
        depth = 1
