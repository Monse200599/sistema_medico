# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.empleados import views
from django.http import HttpResponse
urlpatterns = [
    path('', views.listar_empleados, name='listar_empleados'),
    path('agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('actualizar/<int:pk>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('eliminar/<int:pk>/', views.eliminar_empleado, name='eliminar_empleado'),
]
