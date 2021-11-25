# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.areas import views
from django.http import HttpResponse
urlpatterns = [
    path('', views.listar_areas, name = 'listar_areas'),
    path('agregar/', views.agregar_area, name='agregar_area'),
    path('actualizar/<int:pk>/', views.actualizar_area, name ='actualizar_area'),
    path('eliminar/<int:pk>/', views.eliminar_area, name='eliminar_area'),
]
