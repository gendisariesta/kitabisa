from django.urls import path
from . import views

app_name = 'ranking'
urlpatterns = [
    path('', views.index, name='index'),
    path('kriteria', views.kriteria, name='kriteria'),
    path('crips', views.crips, name='crips'),
    path('alternatif', views.alternatif, name='alternatif'),
    path('bobot', views.bobot, name='bobot'),
    path('perhitungan', views.perhitungan, name='perhitungan'),
]