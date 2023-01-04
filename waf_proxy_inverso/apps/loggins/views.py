from django.shortcuts import render
from .models import Systemevents
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url='Login')
def index_view(request):
    systemevents = Systemevents.objects.all()
    print(systemevents)
    data = {}
    return render(request, 'loggins/index.html', data)
