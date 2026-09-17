from django.urls import path
from . import views

urlpatterns = [
    path('', views.detalle, name='detalle'),
    path('error/', views.error_juego, name='error_juego'),
    path('<int:id>/', views.detalle, name='detalle_juego'),
]
