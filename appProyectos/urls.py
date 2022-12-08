from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import index,ProyectoCreate

urlpatterns = [
    path('register/',login_required(ProyectoCreate.as_view()) , name='proyecto-register'),
]
