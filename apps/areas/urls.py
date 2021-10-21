# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.areas.views import AreasListado, AreaDetalle, AreaCrear, AreaActualizar, AreaEliminar
from django.http import HttpResponse
urlpatterns = [
    # path('', views.index, name = 'areas'),
    # path('create/', views.create, name = 'crear'),
    
    
    # URLs del usaruio final
    path('', AreasListado.as_view(template_name = "areas/index.html"), name='leer'),
    path('detalle/<int:pk>/', AreaDetalle.as_view(template_name = "areas/detalles.html"), name='detalles'), 
    path('crear/', AreaCrear.as_view(template_name = "areas/create.html"), name='crear'),
    path('editar/<int:pk>/', AreaActualizar.as_view(template_name = "areas/update.html"), name='actualizar'),    
    path('eliminar/<int:pk>/', AreaEliminar.as_view(), name='eliminar'),

    # URLs para los sensores
]
