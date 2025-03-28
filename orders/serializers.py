from rest_framework import serializers
from .models import Order, OrderDetail
from products.models import Product

class OrderDetailSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='producto')
    
    class Meta:
        model = OrderDetail
        fields = ('product', 'qty')
        read_only_fields = ('order', 'subtotal')

class OrderSerializer(serializers.ModelSerializer):
    products = OrderDetailSerializer(many=True, write_only=True)
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('total',)

    def create(self, validated_data):
        details_data = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        total = 0

        for item in details_data:
            order_detail = OrderDetail.objects.create(
                order=order,
                producto=item['producto'],
                qty=item['qty']
            )
            total += order_detail.subtotal
        order.total = total
        order.save()
        return order

