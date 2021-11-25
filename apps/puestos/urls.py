# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.puestos import views
from django.http import HttpResponse
urlpatterns = [
    path('', views.listar_puestos, name='listar_puestos'),
    path('agregar/', views.agregar_puesto, name='agregar_puesto'),
    path('actualizar/<int:pk>/', views.actualizar_puesto, name='actualizar_puesto'),
    path('eliminar/<int:pk>/', views.eliminar_puesto, name='eliminar_puesto'),
]
