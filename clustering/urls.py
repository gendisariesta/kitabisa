from django.urls import path
from . import views

app_name = 'clustering'
urlpatterns = [
    path('', views.index, name='index'),
    path('proses', views.proses, name='proses'),
]