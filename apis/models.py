from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  
    entrence = models.IntegerField()
    row = models.IntegerField()
    number = models.IntegerField()
    expiration_date = models.DateField() 
    def __str__(self):
        return self.name

    def is_active(self):
        return self.expiration_date >= models.DateField.today()

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shops = models.ManyToManyField(Shop, related_name='products')  

    def __str__(self):
        return self.name

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, related_name='sellers', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username