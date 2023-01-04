from django.contrib import admin
from django.urls import path, include
from .apps.administrator.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='Login'),
    path('logout/', logout_view, name='Logout'),
    path('', include('waf_proxy_inverso.apps.dashboard.urls')),
    path('loggins/', include('waf_proxy_inverso.apps.loggins.urls')),
    path('admin-site/', include('waf_proxy_inverso.apps.administrator.urls')),
]
