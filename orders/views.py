from rest_framework import serializers
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Order, OrderDetail
from .serializers import OrderSerializer, OrderDetailSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer