from django.shortcuts import render
from django.http import HttpResponse
from dtks.models import Bansos

from django.contrib.auth.decorators import login_required
from account.decorators import unauthenticated_user, allowed_users

def index(request):
  
  context={
  }
  return render(request, 'landing_page.html', context)

@login_required(login_url='account:login')
@allowed_users(allowed_roles=['Admin','Superadmin'])
def dashboard(request):
  bansos = Bansos.objects.all()
  context={
    'bansos':bansos
  }
  return render(request, 'index.html', context)