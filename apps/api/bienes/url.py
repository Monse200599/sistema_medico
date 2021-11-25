from rest_framework.routers import DefaultRouter
from apps.api.bienes.views import BienesViewSet

router_bienes = DefaultRouter()
router_bienes.register(prefix='bienes', basename='bienes', viewset=BienesViewSet)
