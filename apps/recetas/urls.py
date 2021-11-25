from django.urls import path
from apps.recetas import views
urlpatterns = [
    path('', views.listar_recetas, name='listar_recetas'),
    path('agregar/', views.agregar_receta, name='agregar_receta'),
    path('actualizar/<int:pk>/', views.actualizar_receta, name='actualizar_receta'),
    path('eliminar/<int:pk>/', views.eliminar_receta, name='eliminar_receta'),
]
