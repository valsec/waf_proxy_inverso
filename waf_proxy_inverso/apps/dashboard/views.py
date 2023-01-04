from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from ..loggins.models import Systemevents

@login_required(login_url='Login')
def index_view(request):
    user_group = request.user.groups.values_list('name', flat=True)
    count = []
    for d in user_group:
        dlist = d.split('.')
        dwaf = f"{dlist[0]}-modsec:"
        dlog = f"{dlist[0]}:"
        
        log_waf = Systemevents.objects.filter(syslogtag__startswith=dwaf).filter(message__startswith=' ModSecurity:').count()
        log_access = Systemevents.objects.filter(syslogtag=dlog).count()
        
        count.append((d, log_access, log_waf))

    data = {
        'data': count,
    }
    return render(request, 'dashboard/index.html', data)

