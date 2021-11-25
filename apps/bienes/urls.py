from django.urls import path
from apps.bienes import views
urlpatterns = [
    path('', views.listar_bienes, name='listar_bienes'),
    path('agregar/', views.agregar_bienes, name='agregar_bienes'),
    path('actualizar/<int:pk>/', views.actualizar_bienes, name='actualizar_bienes'),
    path('eliminar/<int:pk>/', views.eliminar_bienes, name='eliminar_bienes'),
]