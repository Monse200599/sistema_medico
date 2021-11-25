from rest_framework.serializers import ModelSerializer
from apps.bitacoras.models import Bitacora


class BitacoraSerializer(ModelSerializer):
    class Meta:
        model = Bitacora
        fields = ['cantidad',
                  'fecha',
                  'hora',
                  'entrada',
                  'usuario',
                  'receta',
                  'bienes',
                  'area',
                  ]
    
