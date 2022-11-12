from django.urls import path
from app import views

urlpatterns = [
    path('', views.index),
    path('socios/', views.listadoSocios),
    path('agregar/', views.agregarSocio),
    path('actualizar/<int:id>', views.actualizarsocio),
    path('eliminar/<int:id>', views.eliminarsocio),
]