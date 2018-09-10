from django.db import models


# Create your models here.

class Register(models.Model):
    username =  models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    name = models.CharField(max_length=15)
    surname  = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Phones(models.Model):
    Brand = models.CharField(max_length=20,unique=True)
    model = models.CharField(max_length=20)
    serial_number = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField(max_length=10)
    quantity = models.IntegerField(max_length=10)

    def __str__(self):
        return self.Brand


class Categories(models.Model):
    name = models.CharField(max_length=20)
    Brand = models.ForeignKey(Phones,to_field='Brand',on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=20)
    description = models.TextField(max_length=40)

    def __str__(self):
         return self.name



