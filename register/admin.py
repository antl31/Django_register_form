from django.contrib import admin

from register.models import Register,Phones,Categories
# Register your models here.

admin.site.register(Register)
admin.site.register(Phones)
admin.site.register(Categories)

