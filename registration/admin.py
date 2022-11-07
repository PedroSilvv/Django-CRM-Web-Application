from django.contrib import admin
from .models import CustomUser, Setor


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'setor')


admin.site.register(Setor)
admin.site.register(CustomUser, UserAdmin)
