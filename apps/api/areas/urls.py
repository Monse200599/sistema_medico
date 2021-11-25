from rest_framework.routers import DefaultRouter
from apps.api.areas.views import AreasViewSet

router_area = DefaultRouter()
router_area.register(prefix='areas', basename='areas', viewset=AreasViewSet)