from rest_framework.serializers import ModelSerializer
from apps.puestos.models import Puesto

class PuestoSerializer(ModelSerializer):
    class Meta:
        model = Puesto
        fields = ['nombre',]
