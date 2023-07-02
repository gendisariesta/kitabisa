from django.shortcuts import render
from django.http import HttpResponse
from dtks.models import Bansos
from penerima.models import Penerima, Ranking

from django.contrib.auth.decorators import login_required
from account.decorators import unauthenticated_user, allowed_users

def index(request):
  
  context={
    'title':"Sistem Bansos",
  }
  return render(request, 'landing_page.html', context)

@login_required(login_url='account:login')
@allowed_users(allowed_roles=['Admin','Superadmin'])
def dashboard(request):
  bansos = Bansos.objects.all()
  tahun = Penerima.objects.values_list('tahun', flat=True).distinct()

  penerima = []
  for p in tahun:
      count = Penerima.objects.filter(tahun = p).count()
      penerima.append(count)
  pmks = []
  for p in tahun:
      count = Ranking.objects.filter(tahun = p).count()
      pmks.append(count)
  context={
    'title':"Dashboard",
    'bansos':bansos,
    'penerima' : penerima,
    'tahun':tahun,
    'pmks':pmks
  }
  return render(request, 'index.html', context)