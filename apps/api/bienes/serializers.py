from rest_framework.serializers import ModelSerializer
from apps.bienes.models import Bienes


class BienesSerializer(ModelSerializer):
    class Meta:
        model = Bienes
        fields = ['tipo',
                  'num_unidades',
                  'num_cajas',
                  'lote',
                  'caducidad',
                  'tipo_bienes',
                  ]
