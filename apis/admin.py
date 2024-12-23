from django.contrib import admin
from .models import Shop, Product, Seller

class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'expiration_date']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

class SellerAdmin(admin.ModelAdmin):
    list_display = ['user', 'shop']

admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Seller, SellerAdmin)
