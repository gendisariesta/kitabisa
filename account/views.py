from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

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
        return redirect ('login')
  # if request.method=="GET":
  #     if request.user.is_authenticated():
  #       return redirect ('data_bansos:sembako_lansia')
  #     else:
  return render(request, 'account/login.html', context)

def logoutView(request):
  context={
    'title':'Logout',
  }
  
  logout(request)
  return redirect('account:login')