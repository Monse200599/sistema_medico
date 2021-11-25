from rest_framework.serializers import ModelSerializer
from apps.recetas.models import Receta

class RecetaSerializer(ModelSerializer):
    class Meta:
        model = Receta
        fields = [
            'cantidad',
            'fecha',
            'personal',
            'bienes',
        ]
