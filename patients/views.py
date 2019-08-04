""" view for patients """

from django.views.generic import ListView
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer


class PatientList(ListView):
    """ docstring for patientList """
    model = Patient


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
