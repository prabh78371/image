from django.contrib import admin
from .models import Image

# Register your models here.
admin.site.register(Image)
class Imageadmin(admin.ModelAdmin):
    list_display = ['id','photo','date']
    
