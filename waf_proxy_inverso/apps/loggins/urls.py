from django.urls import path
from .views import index_view

app_name = 'Loggins'

urlpatterns = [
    path('', index_view, name='Index'),
]