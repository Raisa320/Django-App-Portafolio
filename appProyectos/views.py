from django.shortcuts import  redirect, render
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from appProyectos.forms import  ProyectoForm
from django.contrib import messages

from appProyectos.models import Proyecto
# Create your views here.
@login_required
def index(request):
    context={}
    return render(request,"proyecto/index.html",context)
    

class ProyectoCreate(CreateView):
    form_class=ProyectoForm
    template_name = 'proyecto/form-proyecto.html'
    success_url = '/'
    
    def form_valid(self,form):
        print("hola")
        form.instance.autor=self.request.user
        return super().form_valid(form)
