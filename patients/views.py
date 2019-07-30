""" view for patients """

from django.views.generic import ListView
from .models import Patient


class PatientList(ListView):
    """ docstring for patientList """
    model = Patient
