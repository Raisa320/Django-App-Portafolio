from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from appUser.forms import LoginForm,UserRegisterForm,UserUpdateForm,ProfileUpdateForm

# Create your views here.
def registerPage(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'¡Tu cuenta ha sido creada! Puedes iniciar sesión')
            return redirect('login-page')
    else:
        form=UserRegisterForm()
    context={}
    context["form"]=form
    return render(request,"user/register-user.html",context)

def loginPage(request):
    context={}
    context["form"]=LoginForm()
    return render(request,"user/login.html",context)
    
@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'¡Tu cuenta ha sido actualizada!')
            return redirect('user-profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        "u_form":u_form,
        "p_form":p_form
    }

    return render(request,'user/profile.html',context)