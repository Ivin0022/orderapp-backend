from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer, OrderListSerializer
from patients.serializers import PatientSerializer


class OrderListView(ListView):
    model = Order


class OrderDetailView(DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        """ used to update the status to seen when the details
            of the current object are view
            basically a hack so i don't have to write a 
            function based view to handle the both rendering
            the details and updating status 
        """
        current_object: Order = kwargs['object']

        # don't set the status to seen if already fulfilled
        print(current_object.status)
        if current_object.status != Order.STAUTS_FULFILLED:
            Order.set_status(current_object.pk, Order.STAUTS_SEEN)

        return super().get_context_data(**kwargs)


def hander(request, pk):
    Order.set_status(pk, Order.STAUTS_FULFILLED)
    return redirect('orders:home')


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # overriding this function instead of list()
    # since the only this changing is the serializer class
    # retrive use the same serializer as list
    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return OrderListSerializer
        return super().get_serializer_class()
