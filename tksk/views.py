from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from dtks.models import Anggota, Bansos, Kecamatan, Rumah, Aset, Kondisi_Rumah

# Create your views here.
def index(request):
    context={
        'title': 'Dashboard TKSK'
    }
    return render (request, 'tksk/index.html', context)

def input(request):
    data_rumah = Rumah.objects.filter(kecamatan__nama_kecamatan=request.user.location)
    data_aset = Aset.objects.all()
    context={
        'title': 'Input Data',
        'data_rumah': data_rumah,
        'data_aset': data_aset
    }
    return render (request, 'tksk/input.html', context)

