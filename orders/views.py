from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import redirect, get_object_or_404
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer


class OrderListView(ListView):
    model = Order


class OrderDetailView(DetailView):
    model = Order


def hander(request, pk):
    Order.set_status(pk, Order.STAUTS_FULFILLED)
    return redirect('orders:home')


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
