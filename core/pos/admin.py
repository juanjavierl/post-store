from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([Category, Company,Product,Orden,Pedido,Client])