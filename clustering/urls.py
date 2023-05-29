from django.urls import path
from . import views

app_name = 'clustering'
urlpatterns = [
    path('', views.index, name='index'),
    path('proses', views.proses, name='proses'),
    path('proses/<str:name>', views.proses_cluster, name='proses_cluster'),
    path('analisis_cluster', views.analisis_cluster, name='analisis_cluster'),
    path('hasil', views.hasil, name='hasil'),
]