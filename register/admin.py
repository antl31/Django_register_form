from django.contrib import admin

from mysite.register.models import Register,Phones,Products
# Register your models here.

admin.site.mysite.register(Register)
admin.site.mysite.register(Phones)
admin.site.mysite.register(Products)

