from django.shortcuts import render, redirect
from dtks.models import Anggota, Bansos, Kecamatan
from .models import Penerima

# Create your views here.
def index(request, slug):
    # bansos = Bansos.objects.get(slug=slug)
    bansos = Bansos.objects.all()
    penerima = Penerima.objects.filter(bansos__slug__contains=slug)
    context={
        'title':'Daftar Penerima',
        'penerima':penerima,
        'bansos':bansos
    }
    return render(request, 'penerima/index.html', context)

def detail(request, id):
    penerima = Penerima.objects.get(id=id)
    bansos = Bansos.objects.all()
    # bansos=Penerima.objects.filter(anggota_id=id).order_by('tahun')
    
    context={
        'title':'Detail Penerima',
        # 'data_anggota': anggota,
        'penerima':penerima,
        'bansos':bansos,
        
    }
    return render(request, 'penerima/detail_penerima.html', context)
