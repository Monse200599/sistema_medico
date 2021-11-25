from rest_framework.routers import DefaultRouter
from apps.api.bitacoras.views import BitacoraViewSet

router_bitacoras = DefaultRouter()
router_bitacoras.register(prefix='bitacoras', basename='bitacoras', viewset=BitacoraViewSet)
