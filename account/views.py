from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from . models import User
# from django.contrib.auth.models import User

# Create your views here.

def loginView(request):
  context={
        'title':'Login',
    }
  user=None
  if request.method=='POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      
      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)
        return redirect ('dashboard')
      else:
        return redirect ('account:login')
  # if request.method=="GET":
  #     if request.user.is_authenticated():
  #       return redirect ('data_bansos:sembako_lansia')
  #     else:
  return render(request, 'account/login.html', context)

def logoutView(request):
  
  logout(request)
  return redirect('account:login')

def user(request):
  user = User.objects.all()
  # if User.objects.filter(role='Pimpinan'):
  #   badge="primary"
  # elif role == 'Pimpinan':
  #   badge="success"
  # else :
  #   badge = "warning"
  context = {
    'title' : 'User',
    'user'  : user,
    'badge' : 'success',
    'no'    : 1,
  }
  if request.method == 'POST':
    nama = request.POST['nama']
    username = request.POST['username']
    password = request.POST['password']
    location = request.POST['location']
    # new_user = User(name=nama,username=username,password=password,role=role,location=location)
    new_user=User.objects.create_user(name=nama,username=username,location=location)
    new_user.set_password(password)
    new_user.save()
    return redirect ('account:user')
  
  return render(request, 'account/user.html', context)

def delete(request, id):
  User.objects.filter(id=id).delete()
  return redirect ('account:user')

def update(request, id):
  
  if request.method == 'POST':
    newnama = request.POST['newnama']
    newusername = request.POST['newusername']
    # newpassword = request.POST['newpassword']
    newlocation = request.POST['newlocation']
    user = User.objects.get(id=id)
    user.name = newnama
    user.username = newusername
    user.location = newlocation
    # user.set_password(newpassword)
    user.save()
    return redirect ('account:user')