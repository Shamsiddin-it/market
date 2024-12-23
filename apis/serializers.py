from rest_framework import serializers
from .models import Shop, Product, Seller, Category



class ProductSerializer(serializers.ModelSerializer):
    # shops = ShopSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category','price', 'shops']

class CategorySerializer(serializers.ModelSerializer):
    category_product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'category_product']

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
