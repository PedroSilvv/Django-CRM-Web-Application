from django.contrib import admin
from .models import Create_CRM


class CreateCRMAdmin(admin.ModelAdmin):
    list_display = ("id", "data", "empresa")

admin.site.register(Create_CRM)
