from django.shortcuts import render
from django.http import HttpResponse
from dtks.models import Bansos
from penerima.models import Penerima, Ranking
from dtks.models import Kecamatan,Rumah, Anggota

from django.contrib.auth.decorators import login_required
from account.decorators import unauthenticated_user, allowed_users

@unauthenticated_user
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
  kecamatan = Kecamatan.objects.all()
  data_kecamatan = []
  for kec in kecamatan:
    count_anggota = []
    rumah = Rumah.objects.filter(kecamatan=kec).values()
    for r in rumah:
      i = 0
      count = Anggota.objects.filter(rumah=r.get("id")).count()
      i=i+count
      count_anggota.append(i)  
    a = sum(count_anggota)
    data_kecamatan.append({"kec":kec,"count":a})
    
  
  bansos_disabilitas = Bansos.objects.get(nama_bansos='Sembako Disabilitas')
  bansos_lansia = Bansos.objects.get(nama_bansos='Sembako Lansia')

  disabilitas_penerima = Ranking.objects.filter(bansos=bansos_disabilitas).filter(status='Penerima').count()
  disabilitas_disetujui = Ranking.objects.filter(bansos=bansos_disabilitas).filter(status="Disetujui").count()
  count_disabilitas_diterima = disabilitas_penerima + disabilitas_disetujui
  count_disabilitas_ditolak = Ranking.objects.filter(bansos=bansos_disabilitas).filter(status="Ditolak").count()
  lansia_penerima = Ranking.objects.filter(bansos=bansos_lansia).filter(status='Penerima').count()
  lansia_disetujui = Ranking.objects.filter(bansos=bansos_lansia).filter(status="Disetujui").count()
  count_lansia_diterima = lansia_penerima + lansia_disetujui
  count_lansia_ditolak = Ranking.objects.filter(bansos=bansos_lansia).filter(status="Ditolak").count()
  jumlah_pmks = Anggota.objects.all().count()

  penerima_pmks = []
  for kec in kecamatan :
    penerima_count = []
    pmks_count = []
    for p in tahun:
      count_penerima = Penerima.objects.values_list('anggota', flat=True).filter(anggota__rumah__kecamatan=kec).filter(tahun = p).distinct().count()
      penerima_count.append(count_penerima)
    for p in tahun:
      count_pmks = Ranking.objects.values_list('anggota', flat=True).filter(anggota__rumah__kecamatan=kec).filter(tahun = p).distinct().count()
      pmks_count.append(count_pmks)
    penerima_pmks.append({'penerima':penerima_count, 'pmks':pmks_count, 'kec':kec, 'tahun':p})

    penerima = []
    for p in tahun:
        count = Penerima.objects.values_list('anggota', flat=True).filter(tahun = p).count()
        penerima.append(count)
    pmks = []
    for p in tahun:
        count = Ranking.objects.values_list('anggota', flat=True).filter(tahun = p).distinct().count()
        pmks.append(count)
  context={
    'title':"Dashboard",
    'bansos':bansos,
    'penerima_pmks' : penerima_pmks,
    'tahun':tahun,
    'penerima':penerima,
    'pmks':pmks,
    'kecamatan' :kecamatan,
    'data_kecamatan':data_kecamatan,
    'count_pmks':jumlah_pmks,
    'count_disabilitas_diterima':count_disabilitas_diterima,
    'count_disabilitas_ditolak':count_disabilitas_ditolak,
    'count_lansia_diterima':count_lansia_diterima,
    'count_lansia_ditolak':count_lansia_ditolak,

  }
  return render(request, 'index.html', context)