from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Customer, Order, OrderItem
from .serializers import CustomerSerializer, OrderSerializer, OrderItemSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()    
    serializer_class = OrderSerializer
