from django.contrib import admin
from .models import *
# Register your models here.
reg = [order,competition]
for i in reg:
	admin.site.register(i)