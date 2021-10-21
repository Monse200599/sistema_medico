from django.contrib import admin
from apps.puestos.models import Puesto
@admin.register(Puesto)
class PuestoAdmin(admin.ModelAdmin):
    pass
