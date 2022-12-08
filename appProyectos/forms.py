from django import forms

from appProyectos.models import Proyecto

class ProyectoForm(forms.ModelForm):
    """ProyectoForm definition."""

    # TODO: Define form fields here
    # Título del proyecto
    title = forms.CharField(label="Titulo", max_length=200, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    #Descripción del proyecto
    descripcion=forms.CharField(label="Descripción",widget=forms.Textarea(attrs={'class': 'form-control',"rows":3}))
    #Tags: HTML, CSS, PYTHON, etc
    tags = forms.CharField(label="Tags",max_length=100, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    #Foto (que puede ser una URL)
    foto = forms.URLField(label="Foto",required=True,widget=forms.URLInput(attrs={'class': 'form-control',"placeholder":"https://..."}))
    #URL de github
    git = forms.URLField(label="Url de Git",required=True,widget=forms.URLInput(attrs={'class': 'form-control',"placeholder":"https://..."}))
    #Formulario con validación
    class Meta:
        model=Proyecto #USER DE DJANGO
        fields=['title','descripcion','tags','foto','git']

