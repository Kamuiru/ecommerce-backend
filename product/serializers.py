from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'get_image',
            'get_thumbnail',
            'price',
            'get_absolute_url'
        ]

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'products',
            'get_absolute_url',
        ]