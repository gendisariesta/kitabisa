from django.shortcuts import render, redirect
from django.db.models import Avg
from dtks.models import Anggota, Kecamatan, Bansos
from penerima.models import Penerima
# from mapping.filters import PenerimaFilter

import geocoder
import folium
from folium.plugins import HeatMap
from folium.plugins import FastMarkerCluster
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="bytescout", timeout=None)

def getloc_lats_longs(locations):
    loc_lats_longs = []
    for loc in locations:
        loc_lat_long = geolocator.geocode(query = loc+', Purbalingga')
        count = Anggota.objects.filter(rumah__kecamatan__nama_kecamatan = loc).count()
        loc_lats_longs.append([loc_lat_long.latitude, loc_lat_long.longitude, count])
    return loc_lats_longs
# Create your views here.
def index(request):
    #tahun=Penerima.objects.values_list("tahun", flat=True).order_by("tahun").distinct()
    kecamatan = Kecamatan.objects.all()
    bansos = Bansos.objects.all()
    anggota = Anggota.objects.all()
    penerima = Penerima.objects.all()
    nama_kecamatan = Kecamatan.objects.values_list('nama_kecamatan', flat=True)
    avg_lat = Penerima.objects.aggregate(avg=Avg('anggota__rumah__koordinat_lat'))['avg']
    avg_long = Penerima.objects.aggregate(avg=Avg('anggota__rumah__koordinat_long'))['avg']

    #Create Map Object
    m = folium.Map(location=[avg_lat, avg_long], zoom_start= 12)
    
    #cluster marker
    # latitudes = [ang.rumah.koordinat_lat for ang in anggota]
    # longitudes = [ang.rumah.koordinat_long for ang in anggota]
    # FastMarkerCluster(data=list(zip(latitudes, longitudes))).add_to(m)

    #Map Heat
    latitudes = [ang.rumah.koordinat_lat for ang in anggota]
    longitudes = [ang.rumah.koordinat_long for ang in anggota]
    HeatMap(data=list(zip(latitudes, longitudes)), radius=50, blur=20).add_to(m)
    # lats_longs = getloc_lats_longs(nama_kecamatan)
    # HeatMap(lats_longs, radius=40, blur=20).add_to(m)
    
    #filter
    # penerima_filter=PenerimaFilter(request.POST, queryset=Penerima.objects.all())
    # penerima=penerima_filter.qs

    # image_name='bansos.jpg'
    # image=static('mapping/leaflet/images/')+image_name
    #marker anggota
    # for marker in anggota:
    #     folium.Marker([marker.rumah.koordinat_lat, marker.rumah.koordinat_long]).add_to(m)
    #marker penerima
    for marker in penerima:
        folium.Marker([marker.anggota.rumah.koordinat_lat], tooltip='Click for more',
                        popup='<b>Nama : </b>'+marker.anggota.nama_art+'<br>'+'<b>Kecamatan : </b>'+marker.anggota.rumah.kecamatan.nama_kecamatan+
                        '<br><b>Desa : </b>'+marker.anggota.rumah.desa+'<br><b>Menerima sebanyak 3 kali</b><br><b>Bansos : </b>'+
                        marker.bansos.nama_bansos+'<hr style="border: solid green 4px;opacity: 100;margin-top:10px; margin-bottom:10px;width: 150px;"><a href="#">Detail |</a><a href="http://maps.google.com/?q='+marker.anggota.rumah.koordinat_lat+'"target="_blank"> Route</a>',
                        icon=folium.Icon(color=marker.bansos.color, icon='')).add_to(m)
    #get HTML representation of map object
    m = m._repr_html_()
    
    context={
    'title': 'Mapping',
    'm' : m,
    'kecamatan':kecamatan,
    # 'tahun':tahun,
    'bansos':bansos,
    'form':penerima_filter.form,
    }
    return render (request, 'mapping/index.html', context)

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
    