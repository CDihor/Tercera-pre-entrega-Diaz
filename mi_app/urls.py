from django.urls import path
from . import views


urlpatterns = [
    path('listar/', views.lista_objetos, name='lista_objetos'),
    path('agregar/', views.agregar_objeto, name='agregar_objeto'),
    path('buscar/', views.buscar_objeto, name='buscar_objeto'),
]

