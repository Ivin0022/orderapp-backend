""" patient admin """

from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget, PhoneNumberPrefixWidget
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import DateField
from django.forms.widgets import SelectDateWidget
from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    '''Admin View for Patient'''

    list_display = ('name', 'age', 'case_no', 'mobile', 'address')
    search_fields = ('name', 'mobile',)

    formfield_overrides = {
        PhoneNumberField: {'widget': PhoneNumberPrefixWidget},
        DateField: {'widget': SelectDateWidget},
    }
