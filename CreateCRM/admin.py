from django.contrib import admin
from .models import Create_CRM


class CreateCRMAdmin(admin.ModelAdmin):
    list_display = ("id", "data_criacao", "empresa", "mostrar_crm", "versao")

admin.site.register(Create_CRM, CreateCRMAdmin)
