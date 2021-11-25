from apps.bienes import views
from django.urls import path
from apps.bitacoras import views

urlpatterns = [
    path('', views.listar_bitacoras, name='listar_bitacoras'),
    path('agregar/', views.agregar_bitacora, name='agregar_bitacora'),
    path('actualizar/<int:pk>/', views.actualizar_bitacora, name='actualizar_bitacora'),
    path('eliminar/<int:pk>/', views.eliminar_bitacora, name='eliminar_bitacora'),
]
