# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.bienes.views import BienesListado, BienesDetalle, BienesCrear, BienesActualizar, BienesEliminar
from django.http import HttpResponse

urlpatterns = [
    path('', BienesListado.as_view(template_name = "bienes/index.html"), name='leer'),
    path('detalle/<int:pk>/', BienesDetalle.as_view(template_name = "bienes/detalles.html"), name='detalles'), 
    path('crear/', BienesCrear.as_view(template_name = "bienes/create.html"), name='crear'),
    path('editar/<int:pk>/', BienesActualizar.as_view(template_name = "bienes/update.html"), name='actualizar'),    
    path('eliminar/<int:pk>/', BienesEliminar.as_view(), name='eliminar'),
]
