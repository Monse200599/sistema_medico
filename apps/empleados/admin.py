# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User

from apps.empleados.models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    pass

class EmpleadoInline(admin.StackedInline):
    model = Empleado
    can_delete = False
    verbose_name_plural = 'Empleados'

class UserAdmin(BaseUserAdmin):
    inlines = (EmpleadoInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)