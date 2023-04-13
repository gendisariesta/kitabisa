from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login', views.login, name='login'),
    path('user', views.registerPage, name='user'),
]