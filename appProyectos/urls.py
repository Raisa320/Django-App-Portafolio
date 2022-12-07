from django.urls import path

from .views import index,proyectForm

urlpatterns = [
    path('proyecto-register/', proyectForm, name='proyecto-register'),
]
