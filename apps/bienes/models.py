from django.db import models
# Create your models here.
class Bienes(models.Model):
    BIENES_CHOICES = (
        ('INS', 'Insumo'),
        ('MED', 'Medicamento'),
    )

    tipo = models.CharField(max_length=255)
    num_unidades = models.PositiveIntegerField()
    num_cajas = models.PositiveIntegerField()
    lote = models.CharField(max_length=12)
    caducidad = models.DateField()
    tipo_bienes = models.CharField(max_length=3, choices=BIENES_CHOICES)
    codigo_barras = models.ImageField(null = True)