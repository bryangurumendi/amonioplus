from . import views
from django.contrib import admin
from django.urls import path

app_name = 'persona_app'

urlpatterns = [
    # PAGINA DE INICIO
    path(
        '',
        views.PedidoAmonio.as_view(),
        name='inicio',
    ),
]