from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from apps.recetas.models import Receta
from apps.bienes.models import Bienes
from apps.areas.models import Area
# Create your models here.
class Bitacora(models.Model):
    cantidad = models.PositiveIntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    entrada = models.BooleanField()
    usuario = models.ForeignKey(User, on_delete=CASCADE)
    receta = models.ForeignKey(Receta, on_delete=CASCADE)
    bienes = models.ForeignKey(Bienes, on_delete=CASCADE)
    area = models.ForeignKey(Area, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
