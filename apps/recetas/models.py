from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from apps.bienes.models import Bienes

class Receta(models.Model):
    cantidad = models.PositiveIntegerField()
    fecha = models.DateField()
    personal = models.ForeignKey(User, on_delete=CASCADE)
    bienes = models.ForeignKey(Bienes, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)