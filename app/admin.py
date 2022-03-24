from django.contrib import admin

# Register your models here.
from .models import *

class UploadAdmin(admin.ModelAdmin):
    list_display = ("user",)

admin.site.register(upload, UploadAdmin)