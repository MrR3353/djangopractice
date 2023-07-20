from django.contrib import admin
from .models import Order, StatusCrm

# Register your models here.
admin.site.register(Order)
admin.site.register(StatusCrm)