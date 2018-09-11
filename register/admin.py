from django.contrib import admin

from .models import Register, Phones, Categories
# Register your models here.

admin.site.register(Register)
admin.site.register(Phones)
admin.site.register(Categories)

