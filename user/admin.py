from django.contrib import admin
from .models import worker,client,Profile
# Register your models here.
admin.site.register(worker)
admin.site.register(client)
admin.site.register(Profile)
