from django.contrib import admin

# Register your models here.

from .models import Dive_Site, Diver

admin.site.register(Dive_Site)
admin.site.register(Diver)
