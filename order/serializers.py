from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'product'
            'price',
            "quantity",
        ]

class OrderSerializer(serializers.ModelSerializer):
    orders = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = [
            'paid_amount',
            "phone ",
            "card_number",
            "card_name",
            "created_at"
            'orders'
        ]
    def create(self, validated_data):
        items_data = validated_data.pop('orders')

        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
            
        return order