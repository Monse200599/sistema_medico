from django.contrib import admin
from apps.bitacoras.models import Bitacora
# Register your models here.
@admin.register(Bitacora)
class BitacoraAdmin(admin.ModelAdmin):
    pass
