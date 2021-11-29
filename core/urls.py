# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from apps.api.areas.urls import router_area
from apps.api.bienes.url import router_bienes
from apps.api.bitacoras.url import router_bitacoras
from apps.api.puestos.url import router_puestos
from apps.api.recetas.url import router_recetas

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")),    # Auth routes - login / register
    path("", include("apps.home.urls")),             # UI Kits Html files
    path("areas/", include("apps.areas.urls")),
    path("bienes/", include("apps.bienes.urls")),
    path("bitacoras/", include("apps.bitacoras.urls")),
    path("puestos/", include("apps.puestos.urls")),
    path("recetas/", include("apps.recetas.urls")),
    path("empleados/", include("apps.empleados.urls")),
    path("api/", include(router_area.urls)),
    path("api/", include(router_bienes.urls)),
    path("api/", include(router_bitacoras.urls)),
    path("api/", include(router_puestos.urls)),
    path("api/", include(router_recetas.urls)),
]

