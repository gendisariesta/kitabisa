from django.shortcuts import render, redirect
from dtks.models import Anggota, Bansos, Kecamatan
from .models import Penerima, Ranking

from datetime import datetime

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

def ranking(request):
    ranking=Ranking.objects.all().order_by('status')
    belum_diverifikasi = Ranking.objects.filter(status='Belum Diverifikasi').count()
    penerima = Ranking.objects.filter(status='Penerima').count()
    context={
        'title': 'Perankingan',
        'ranking':ranking,
        'belum_diverifikasi':belum_diverifikasi,
        'penerima':penerima
    }
    return render(request, 'penerima/ranking.html', context)

def disetujui(request, id):
    if request.method == 'POST':
        ranking = Ranking.objects.get(id=id)
        ranking.status = 'Disetujui'
        ranking.save()
        return redirect ('penerima:ranking')

def ditolak(request, id):
    if request.method == 'POST':
        ranking = Ranking.objects.get(id=id)
        ranking.status = 'Ditolak'
        ranking.save()
        return redirect ('penerima:ranking')
    
def proses(request):
    calon_penerima = Ranking.objects.filter(status='Disetujui')[:5]
    if request.method == 'POST':
        for r in calon_penerima:
            ranking = Ranking.objects.get(id=r.id)
            ranking.status = 'Penerima'
            ranking.save()
            penerima = Penerima(
                anggota = Anggota.objects.get(id=r.anggota.id),
                bansos = Bansos.objects.get(nama_bansos='Sembako Lansia'),
                tahun = datetime.now().year
            )
            penerima.save()
        return redirect ('penerima:index', slug='sembako-lansia')
