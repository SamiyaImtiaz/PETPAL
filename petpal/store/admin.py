from django.contrib import admin
from .models import Store , Product ,  GroomingService

# Register your models here.
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(GroomingService)
