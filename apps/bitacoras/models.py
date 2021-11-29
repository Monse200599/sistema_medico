from django.db import models
from django.db.models.deletion import CASCADE
from apps.recetas.models import Receta
from apps.bienes.models import Bienes
from apps.areas.models import Area
from apps.empleados.models import Empleado
# Create your models here.
class Bitacora(models.Model):
    cantidad = models.PositiveIntegerField()
    entrada = models.BooleanField()
    empleado = models.ForeignKey(Empleado, on_delete=CASCADE)
    bienes = models.ForeignKey(Bienes, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_next_status(self, bienes):
        """Método para obtener el siguiente estatus de la entrada/salida"""
        bitacora = Bitacora.objects.filter(bienes=bienes).last()
        if bitacora:
            if self.entrada == True:
                return False
            else:
                return True
        return True
    
    def save(self, *args, **kwarg):
        self.entrada = self.get_next_status(self.bienes)
        super(Bitacora, self).save(*args, **kwarg)
