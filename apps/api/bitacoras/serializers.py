from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.bienes.models import Bienes
from apps.bitacoras.models import Bitacora


class BitacoraSerializer(ModelSerializer):
    bienes = serializers.CharField()
    class Meta:
        model = Bitacora
        fields = ['cantidad',
                  'empleado',
                  'bienes',
                  ]

    def validate(self, attrs):
        try:
            attrs['bienes'] = Bienes.objects.get(codigo_barras=attrs['bienes'])
            return attrs
        except Bienes.DoesNotExist:
            raise serializers.ValidationError("Bien no encontrado")
