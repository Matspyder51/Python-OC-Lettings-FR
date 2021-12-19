from django.contrib import admin
from .models import Letting, Address


# Register your models here.
admin.site.register([Letting, Address])
