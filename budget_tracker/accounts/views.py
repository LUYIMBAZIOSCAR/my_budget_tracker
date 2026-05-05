from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.

# view function to register a user
def register_user(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        form=RegisterForm()

    return render(request,'accounts/register.html',{'form':form})

# view function for login
def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid username or password ')
    else:
        form=AuthenticationForm()

    return render(request,'accounts/login.html',{'form':form})

# view function for logout
def logout_view(request):
    logout(request)
    return redirect('login')


