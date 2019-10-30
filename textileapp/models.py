from django.db import models
from datetime import datetime
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.conf import settings

user = get_user_model()
class Textile(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=None)
    offer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pics', blank=True, default='author.jpg')
class Cart(models.Model):
    title = models.ForeignKey(Textile,on_delete=models.CASCADE,default="",blank=True,null=True)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default="")
    date=models.DateTimeField(default=datetime.now, blank=True)
    totalprice=models.IntegerField(default=None)
    # colour = models.CharField(max_length=200,default=None)
    size=models.IntegerField(default=None)
class Buynow(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    title = models.ForeignKey(Textile, on_delete=models.CASCADE, default="", blank=True, null=True)
    firstname =models.CharField(max_length=100,default=None)
    lastname = models.CharField(max_length=100, default=None)
    state = models.CharField(max_length=200,default=None)
    streetaddress = models.CharField(max_length=500,default=None)
    appartment = models.CharField(max_length=500,default=None)
    town = models.CharField(max_length=200,default=None)
    postcode = models.IntegerField(max_length=6,default=None)
    phone = models.IntegerField(default=None)
    email = models.EmailField(default=None)

class Coupon(models.Model):
    code = models.CharField(max_length=10,default=None)
    couponprice = models.IntegerField(max_length=6,default=None)