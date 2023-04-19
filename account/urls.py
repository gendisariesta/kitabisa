from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('user', views.user, name='user'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
]