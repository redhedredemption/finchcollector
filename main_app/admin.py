from django.contrib import admin

#Import Finch model
from .models import Finch

# Register your models here.
admin.site.register(Finch)