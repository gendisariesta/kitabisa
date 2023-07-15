# Create your views here.
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.conf.urls.static import static
from dtks.models import Rumah, Aset, Kondisi_Rumah, Anggota, Bansos
from penerima.models import Penerima
from .models import Kriteria, Crips
from django.http import HttpResponseRedirect
from datetime import datetime


# Create your views here.
def index(request,slug,tahun):
    kriteria1 = [f.name for f in Kondisi_Rumah._meta.get_fields()]
    kriteria2 = [f.name for f in Anggota._meta.get_fields()]
    nama_kriteria = kriteria1+kriteria2
    bansos = Bansos.objects.all()
    penerima = Penerima.objects.filter(bansos__slug__contains=slug)
    kriteria = Kriteria.objects.all()
    get_bansos = Bansos.objects.get(slug=slug)
    print(slug)
    if request.method == 'POST':
        nama = request.POST.get('nama_kriteria')
        bobot = request.POST.get('bobot')
        atribut = request.POST.get('atribut')
        new_kriteria = Kriteria(nama_kriteria=nama,bobot=bobot,atribut=atribut,bansos=get_bansos)
        new_kriteria.save()  
    context = {
        'bansos':bansos,
        'slug' : slug,
        'penerima':penerima,
        'kriteria':kriteria,
        'nama_kriteria':nama_kriteria,
    }
    return render(request, 'ranking/index.html', context) 

def delete_kriteria(request,slug,id):
    Kriteria.objects.get(id=id).delete()
    return redirect ('ranking:index',slug=slug, tahun = datetime.now().year)