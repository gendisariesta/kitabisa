from django.shortcuts import render, redirect
from dtks.models import Anggota, Kecamatan, Bansos
from .models import Penerima
#from mapping.filter import PenerimaFilter

import folium
from folium.plugins import FastMarkerCluster

# Create your views here.
def index(request):
    #tahun=Penerima.objects.values_list("tahun", flat=True).order_by("tahun").distinct()
    kecamatan = Kecamatan.objects.all()
    bansos = Bansos.objects.all()
    anggota = Anggota.objects.all()
    penerima = Penerima.objects.all()

    #Create Map Object
    m = folium.Map(location=[-7.3653, 109.3707], zoom_start= 12)
    
    #cluster marker
    latitudes = [ang.rumah.koordinat_lat for ang in anggota]
    longitudes = [ang.rumah.koordinat_long for ang in anggota]
    FastMarkerCluster(data=list(zip(latitudes, longitudes))).add_to(m)
    
    #filter
    # penerima_filter=PenerimaFilter(request.POST, queryset=Penerima.objects.all())
    # penerima=penerima_filter.qs

    # image_name='bansos.jpg'
    # image=static('mapping/leaflet/images/')+image_name
    
    #marker penerima
    for marker in penerima:
        folium.Marker([marker.anggota.rumah.koordinat_lat, marker.anggota.rumah.koordinat_long], tooltip='Click for more',
                        popup='<b>Nama : </b>'+marker.anggota.nama_art+'<br>'+'<b>Kecamatan : </b>'+marker.anggota.rumah.kecamatan.nama_kecamatan+
                        '<br><b>Desa : </b>'+marker.anggota.rumah.desa+'<br><b>Menerima sebanyak 3 kali</b><br><b>Bansos : </b>'+
                        marker.bansos.nama_bansos+'<hr style="border: solid green 4px;opacity: 100;margin-top:10px; margin-bottom:10px;width: 150px;"><a href="#">Detail |</a><a href="http://maps.google.com/?q='+marker.anggota.rumah.koordinat_long+','+marker.anggota.rumah.koordinat_long+'"target="_blank"> Route</a>',
                        icon=folium.Icon(color=marker.bansos.color, icon='')).add_to(m)
    #get HTML representation of map object
    m = m._repr_html_()
    
    context={
    'title': 'Mapping',
    'm' : m,
    'kecamatan':kecamatan,
    # 'tahun':tahun,
    'bansos':bansos,
    # 'form':penerima_filter.form,
    }
    return render (request, 'mapping/index.html', context)

def penerima(request, slug):
    # bansos = Bansos.objects.get(slug=slug)
    penerima = Penerima.objects.filter(bansos__slug__contains=slug)
    context={
        'title':'Daftar Penerima',
        'penerima':penerima
    }
    return render(request, 'mapping/penerima.html', context)

def detail(request, id):
    anggota=Anggota.objects.get(id=id)
    bansos=Penerima.objects.filter(anggota_id=id).order_by('tahun')
    
    context={
        'title':'Detail',
        'data_anggota': anggota,
        'bansos':bansos,
        
    }
    return render(request, 'mapping/detail_penerima.html', context)

def bansos(request):
    bansos = Bansos.objects.all()
    if request.method == 'POST':
        nama = request.POST.get('nama')
        kuota = request.POST.get('kuota')
        warna = request.POST.get('warna')
        new_bansos = Bansos(nama_bansos=nama,kuota=kuota,color=warna)
        new_bansos.save()
        return redirect ('mapping:bansos')
    context={
        'bansos':bansos,
    }
    return render(request, 'mapping/bansos.html', context)

def delete_bansos(request, id):
    Bansos.objects.filter(id=id).delete()
    return redirect('mapping:bansos')

def update_bansos(request, id):
  
    if request.method == 'POST':
        newnama = request.POST['newnama']
        newkuota = request.POST['newkuota']
        newwarna = request.POST['newwarna']
        bansos = Bansos.objects.get(id=id)
        bansos.nama_bansos = newnama
        bansos.kuota = newkuota
        bansos.color = newwarna
        # bansos.set_password(newpassword)
        bansos.save()
        return redirect ('mapping:bansos')

def kecamatan(request):
    bansos = Bansos.objects.all()
    kecamatan = Kecamatan.objects.all()
    if request.method == 'POST':
        nama = request.POST['nama']
        kecamatan = Kecamatan(nama_kecamatan=nama)
        kecamatan.save()
        return redirect ('mapping:kecamatan')
    context={
       'bansos':bansos,
       'kecamatan':kecamatan,
    }
    return render(request, 'mapping/kecamatan.html', context)

def delete_kecamatan(request, id):
    Kecamatan.objects.filter(id=id).delete()
    return redirect('mapping:kecamatan')

def update_kecamatan(request, id):
    if request.method == 'POST':
        nama = request.POST['nama']
        kecamatan = Kecamatan.objects.get(id=id)
        kecamatan.nama_kecamatan = nama
        kecamatan.save()
        return redirect ('mapping:kecamatan')
    