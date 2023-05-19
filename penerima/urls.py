from django.urls import path
from . import views

app_name = 'penerima'
urlpatterns = [
    path('<str:slug>', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='detail'),
]