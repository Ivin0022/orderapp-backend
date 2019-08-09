""" models for orders """

from django.db import models
from django.utils import timezone

from patients.models import Patient
from inventory.models import Inventory


class Order(models.Model):
    """ docstring for the class """

    STAUTS_PLACED = 'p'
    STAUTS_SEEN = 's'
    STAUTS_FULFILED = 'f'
    STATUS_CHOICES = (
        (STAUTS_PLACED, 'placed'),
        (STAUTS_SEEN, 'seen'),
        (STAUTS_FULFILED, 'fulfiled'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time_of_placement = models.DateTimeField('order placed', editable=False)
    time_of_fulfilment = models.DateTimeField(
        'order fulfiled',
        editable=False,
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=STAUTS_PLACED
    )
    items = models.ManyToManyField(Inventory)

    @classmethod
    def set_status(cls, pk, status):
        """ setter function for status, was declared to be
            more inline "Fat Models, Thin Views" concept.
            update the status here instead of the Views make 
            it more reusable, without repeating code
            update query doesn't call the save function but 
            instead is directly set using SQL query. so, all 
            the code in the overridden save() isn't called
            hence preventing unwanted/unforeseen side effect
        """
        cls.objects.filter(pk=pk).update(status=status)

    def save(self, *args, **kwargs):
        ''' This method is called every time an object is saved 
            to the datebase, we are overriding it to automatically 
            enter the time of creation, time of fulfilment, set the
            status to placed
        '''

        if self.id is None:
            # checking to see if object exists
            # if id doesn't exists it will be None

            self.time_of_placement = timezone.now()

        elif self.status == self.STAUTS_FULFILED:
            # checking to see if the status of the
            # order as changed to fulfiled

            self.time_of_fulfilment = timezone.now()

        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.patient.name} [{self.patient.case_no}]'
