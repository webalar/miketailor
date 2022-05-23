from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserInfo(models.Model):
    phone = models.CharField(max_length = 10)
    addressline1 = models.CharField(max_length = 100)
    addressline2 = models.CharField(max_length = 100)
    state = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    postalcode = models.CharField(max_length = 6)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email



class Category(models.Model):
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    s_no = models.CharField(max_length=15)
    brand = models.CharField(max_length=15)
    price = models.IntegerField(default=99)
    description = models.CharField(max_length=150)
    color = models.CharField(max_length=30)
    fabric = models.CharField(max_length=30)
    gsm = models.CharField(max_length=30)
    img = models.ImageField(blank=False, upload_to="ProductImages/")

    def __str__(self):
        return self.s_no


class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email



class Order(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    orderID = models.CharField(max_length=10)
    total_price = models.IntegerField(default=0)
    subtotal_price = models.IntegerField(default=0)
    discount_price = models.IntegerField(default=0)

    def __str__(self):
        return self.orderID
