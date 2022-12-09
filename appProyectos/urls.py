from django.urls import path

from .views import ProyectoCreate,ProyectoDetailView,ProyectoUpdate, ProyectoDeleteView

urlpatterns = [
    path('register/',ProyectoCreate.as_view() , name='proyecto-register'),
    path("ver/<int:pk>/", ProyectoDetailView.as_view(), name="proyecto-ver"),
    path("<int:pk>/update/", ProyectoUpdate.as_view(), name="proyecto-update"),
    path("eliminar/<int:pk>/", ProyectoDeleteView.as_view(), name="proyecto-delete"),
]
