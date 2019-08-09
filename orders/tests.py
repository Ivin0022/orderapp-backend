from django.test import TestCase

from .models import Order
from patients.models import Patient


class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        p = Patient(name='django', case_no='170009')
        cls.order = Order(patient=p)

    def test_string_representation(self):
        self.assertEqual(str(self.order), 'django [170009]')
