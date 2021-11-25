from rest_framework.routers import DefaultRouter
from apps.api.puestos.views import PuestoViewSet

router_puestos = DefaultRouter()
router_puestos.register(prefix='puestos', basename='puestos', viewset=PuestoViewSet)
