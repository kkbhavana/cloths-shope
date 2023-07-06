from django.contrib import admin

from .models import Cloths, Category

# Register your models here.
admin.site.register(Cloths)
admin.site.register(Category)