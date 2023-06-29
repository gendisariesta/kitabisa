from django.shortcuts import render, redirect
from dtks.models import Anggota, Bansos, Kecamatan
from .models import Penerima, Ranking
from .filters import TahunFilter
from django.contrib.auth.decorators import login_required
from account.decorators import unauthenticated_user, allowed_users
from datetime import datetime

# Create your views here.
@login_required(login_url='account:login')
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

@login_required(login_url='account:login')
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

def daterange(start, end, step=1):
        current_year = start
        while current_year <= end:
            yield current_year
            current_year += step

@login_required(login_url='account:login')
@allowed_users(allowed_roles=['Superadmin', 'Admin'])
def ranking(request, tahun):
    # tahun_filter=TahunFilter(request.POST, queryset=Ranking.objects.all().order_by('status'))
    # ranking=tahun_filter.qs
    ranking=Ranking.objects.filter(tahun=tahun).order_by('status')
    belum_diverifikasi = Ranking.objects.filter(tahun=tahun).filter(status='Belum Diverifikasi').count()
    penerima = Ranking.objects.filter(tahun=tahun).filter(status='Penerima').count()
    bansos = Bansos.objects.all()
    t = []
            
    for year in daterange(2019, datetime.now().year):
        t.append(year)
    context={
        'title': 'Perankingan',
        'ranking':ranking,
        'belum_diverifikasi':belum_diverifikasi,
        'penerima':penerima,
        'bansos':bansos,
        't':t
        # 'form':tahun_filter.form,
    }
    return render(request, 'penerima/ranking.html', context)

def disetujui(request, id):
    if request.method == 'POST':
        ranking = Ranking.objects.get(id=id)
        ranking.status = 'Disetujui'
        ranking.save()
        return redirect ('penerima:ranking', ranking.tahun)

def ditolak(request, id):
    if request.method == 'POST':
        ranking = Ranking.objects.get(id=id)
        ranking.status = 'Ditolak'
        ranking.save()
        return redirect ('penerima:ranking', ranking.tahun)
    
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
