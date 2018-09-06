from shops.models import Products, Shops

from rest_framework import serializers


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = ('name', 'lat', 'lng')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('title', 'popularity', 'quantity')
