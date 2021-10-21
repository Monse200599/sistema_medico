from django.contrib import admin
from apps.bienes.models import Bienes
# Register your models here.
@admin.register(Bienes)
class BienesAdmin(admin.ModelAdmin):
    pass
