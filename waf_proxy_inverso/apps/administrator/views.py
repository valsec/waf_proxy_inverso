from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def login_view(request):
    mensaje = None
    if request.method == 'POST':
        user_post = request.POST['username']
        pass_post = request.POST['password']
        auth = authenticate(username=user_post, password=pass_post)
        if auth is not None:
            login(request, auth)
            return redirect('Dashboard:Index')
        else:
            mensaje = 'Usuario o Clave Incorrecto.'

    form = LoginForm()
    return render(request, 'login.html', {'mensaje':mensaje, 'form':form})

@login_required(login_url='Login')
def logout_view(request):
    logout(request)
    return redirect('Login')

@login_required(login_url='Login')
def index_view(request):
    data = {}
    return render(request, 'administrator/index.html', data)