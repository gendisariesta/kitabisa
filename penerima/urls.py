from django.urls import path
from . import views

app_name = 'penerima'
urlpatterns = [
    path('<str:slug>', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('ranking/', views.ranking, name='ranking'),
    path('ranking/disetujui/<int:id>', views.disetujui, name='disetujui'),
    path('ranking/ditolak/<int:id>', views.ditolak, name='ditolak'),
    path('ranking/proses', views.proses, name='proses'),
]