from django.contrib import admin
from apps.areas.models import Area
# Register your models here.

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    pass
