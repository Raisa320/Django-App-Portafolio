from django.urls import path

from .views import index,ProyectoCreate

urlpatterns = [
    path('register/',ProyectoCreate.as_view() , name='proyecto-register'),
]
