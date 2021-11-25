from rest_framework.routers import DefaultRouter
from apps.api.recetas.views import RecetaViewSet

router_recetas = DefaultRouter()
router_recetas.register(prefix='recetas', basename='recetas', viewset=RecetaViewSet)
