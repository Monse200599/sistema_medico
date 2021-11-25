from rest_framework.serializers import ModelSerializer
from apps.areas.models import Area

class AreaSerializer(ModelSerializer):

    class Meta:
        model = Area
        fields = ['nombre']
    
