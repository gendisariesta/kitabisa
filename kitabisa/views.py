from django.shortcuts import render
from django.http import HttpResponse
from dtks.models import Bansos

def index(request):
  
  context={
  }
  return render(request, 'landing_page.html', context)

def dashboard(request):
  bansos = Bansos.objects.all()
  context={
    'bansos':bansos
  }
  return render(request, 'index.html', context)