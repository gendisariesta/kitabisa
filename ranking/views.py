# Create your views here.
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.conf.urls.static import static
from dtks.models import Rumah, Aset, Kondisi_Rumah, Anggota, Bansos
# from . models import Jenis
from django.http import HttpResponseRedirect
from django.urls import reverse
import mysql.connector as sql
from django.db import connection
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import base64, urllib
from io import BytesIO

# Create your views here.
def index(request):
    return render(request, 'ranking/index.html') 

def kriteria(request):
    return render(request, 'ranking/kriteria.html')

def crips(request):
    return render(request, 'ranking/crips.html')

def alternatif(request):
    return render(request, 'ranking/alternatif.html')

def bobot(request):
    return render(request, 'ranking/bobot.html')

def perhitungan(request):
    return render(request, 'ranking/perhitungan.html')