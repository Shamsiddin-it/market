from django.urls import path
from .views import (

    CategoryListAPIView, 
    CategoryCreateAPIView, 
    CategoryRetrieveAPIView, 
    CategoryUpdateAPIView, 
    CategoryDestroyAPIView,
    
    ShopListAPIView, 
    ShopCreateAPIView, 
    ShopRetrieveAPIView, 
    ShopUpdateAPIView, 
    ShopDestroyAPIView,
    
    ProductListAPIView, 
    ProductCreateAPIView, 
    ProductRetrieveAPIView, 
    ProductUpdateAPIView, 
    ProductDestroyAPIView
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category-retrieve'),
    path('categories/<int:pk>/update/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDestroyAPIView.as_view(), name='category-destroy'),

    path('shops/', ShopListAPIView.as_view(), name='shop-list'),
    path('shops/create/', ShopCreateAPIView.as_view(), name='shop-create'),
    path('shops/<int:pk>/', ShopRetrieveAPIView.as_view(), name='shop-retrieve'),
    path('shops/<int:pk>/update/', ShopUpdateAPIView.as_view(), name='shop-update'),
    path('shops/<int:pk>/delete/', ShopDestroyAPIView.as_view(), name='shop-destroy'),

    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product-retrieve'),
    path('products/<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDestroyAPIView.as_view(), name='product-destroy'),
]
