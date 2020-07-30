from django.contrib import admin
from .models import Information


class InformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')


admin.site.register(Information, InformationAdmin)
