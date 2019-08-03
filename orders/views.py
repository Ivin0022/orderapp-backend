from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import redirect, get_object_or_404
from .models import Order


class OrderListView(ListView):
    model = Order


class OrderDetailView(DetailView):
    model = Order


def hander(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.STAUTS_FULFILED
    order.save()
    return redirect('orders:home')
