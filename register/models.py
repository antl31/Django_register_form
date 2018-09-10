from django.db import models

# Create your models here.

class Register(models.Model):
    username =  models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    name = models.CharField(max_length=15)
    surname  = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)

class Phones(models.Model):
    Brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    serial_number = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField(max_length=10)
    quantity = models.IntegerField(max_length=10)

class Products(models.Model):
    type = models.ForeignKey(Phones,default=1,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    quantity_all = models.IntegerField(max_length=20)


