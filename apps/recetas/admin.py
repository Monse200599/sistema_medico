from django.contrib import admin
from apps.recetas.models import Receta
# Register your models here.
@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    pass
