from django.shortcuts import render,redirect
from .forms import registerForm,loginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


def registe__view(request):
    form=registerForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        first_name=form.cleaned_data.get("first_name")
        last_name=form.cleaned_data.get("last_name")
        email=form.cleaned_data.get("email")


        newUser=User(username=username,first_name=first_name,last_name=last_name,email=email)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,"Siz uğurla qeydiyyatdan keçdiniz")
        return redirect("home")
    context={'form':form,}
    return  render(request,"registe.html",context)



def login__view(request):
    form=loginForm(request.POST or None )
    context={
        'form':form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)

        if user is None:
            return redirect(request,'login.html')
        login(request,user)
        messages.warning(request,"Giris edildi")
        return redirect('home')
        
    return  render(request,"login.html",context)

def logout__view(request):
    logout(request)
    return  redirect("home")

def About__view(request):
    return  render(request,"about.html")


def contact__view(request):
    return  render(request,"contacts.html")