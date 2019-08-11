from rest_framework import serializers

from .models import Order
from patients.serializers import PatientSerializer
from inventory.serializers import InventorySerializer


# TODO see id there is a need to pass in urls
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    """ seprate serializer just for the list function 
        of orders api, only different is that we use
        depth=2 to show the patient name, item names
        and itemType
    """
    class Meta:
        model = Order
        fields = '__all__'
        depth = 2
