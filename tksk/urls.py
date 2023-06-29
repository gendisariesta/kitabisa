from django.urls import path
from . import views

app_name = 'tksk'
urlpatterns = [
    path('dashboard', views.index, name='dashboard'),
    path('input', views.input, name='input'),
]