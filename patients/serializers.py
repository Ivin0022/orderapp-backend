from rest_framework import serializers

from .models import Patient


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['url', 'name', 'age', 'case_no']
