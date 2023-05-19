from django.urls import path
from . import views

app_name = 'tksk'
urlpatterns = [
    path('dashboard', views.index, name='dashboard'),
    path('input', views.input, name='input'),
    path('input_krt', views.input_krt, name='input_krt'),
    path('input_art/<int:id>', views.input_art, name='input_art'),
    path('detailkrt/<int:id>', views.detailkrt, name='detailkrt'),
    path('detailart/<int:id>', views.detailart, name='detailart'),
]