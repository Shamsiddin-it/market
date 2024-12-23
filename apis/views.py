from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from .models import Category, Shop, Product
from .serializers import CategorySerializer, ShopSerializer, ProductSerializer
import django_filters.rest_framework

class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')  
    
    class Meta:
        model = Category
        fields = ['name']  

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]    
    filterset_class = CategoryFilter
    search_fields = ['name']  

class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'


class ShopFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')  
    
    class Meta:
        model = Shop
        fields = ['name']  

class ShopListAPIView(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ShopFilter
    search_fields = ['name']  

class ShopCreateAPIView(generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    lookup_field = 'pk'

class ShopUpdateAPIView(generics.UpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    lookup_field = 'pk'

class ShopDestroyAPIView(generics.DestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    lookup_field = 'pk'



class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')  
    price_min = filters.NumberFilter(field_name='price', lookup_expr='gte') 
    price_max = filters.NumberFilter(field_name='price', lookup_expr='lte')  
    
    class Meta:
        model = Product
        fields = ['name', 'price_min', 'price_max']  

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]    
    filterset_class = ProductFilter
    search_fields = ['name', 'description']  

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
