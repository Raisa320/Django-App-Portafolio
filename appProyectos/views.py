from django.shortcuts import render

from appProyectos.forms import  ProyectoForm

# Create your views here.
def index(request):
    return render(request,"index.html")

def proyectForm(request):
    context={}
    context["form"]=ProyectoForm()
    return render(request,"form-proyecto.html",context)


