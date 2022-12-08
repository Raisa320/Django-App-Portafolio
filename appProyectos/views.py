from django.shortcuts import  redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from appProyectos.forms import  ProyectoForm
from django.contrib import messages

from appProyectos.models import Proyecto
# Create your views here.
@login_required
def index(request):
    current_user=request.user
    context={
        "proyectos": current_user.proyecto_set.all(),
        "cantidad":current_user.proyecto_set.count()
    }

    return render(request,"proyecto/index.html",context)
    

class ProyectoCreate(SuccessMessageMixin,CreateView):
    form_class=ProyectoForm
    template_name = 'proyecto/form-proyecto.html'
    success_url = '/'
    success_message = "Se ha registrado tu proyecto correctamente"

    def form_valid(self,form):
        form.instance.autor=self.request.user
        return super().form_valid(form)
