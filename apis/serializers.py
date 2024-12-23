from rest_framework import serializers
from .models import Shop, Product, Seller, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # shops = ShopSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category','price', 'shops']

class ShopSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many = True, read_only=True)
    class Meta:
        model = Shop
        fields = ['id', 'name', 'owner', 'entrence', 'row', 'number', 'expiration_date', 'products']


class SellerSerializer(serializers.ModelSerializer):
    shop = ShopSerializer(read_only=True)

    class Meta:
        model = Seller
        fields = ['id', 'user', 'shop']
