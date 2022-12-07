from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from appUser.forms import LoginForm,UserRegisterForm

# Create your views here.
def registerPage(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'¡Tú cuenta ha sido creada! Puedes iniciar sesión')
            return redirect('login-page')
    else:
        form=UserRegisterForm()
    context={}
    context["form"]=form
    return render(request,"register-user.html",context)

def loginPage(request):
    context={}
    context["form"]=LoginForm()
    return render(request,"login.html",context)
