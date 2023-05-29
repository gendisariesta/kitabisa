# Create your views here.
from django.shortcuts import render, redirect
from dtks.models import Rumah, Aset, Kondisi_Rumah
from . models import Jenis
from django.http import HttpResponseRedirect
from django.urls import reverse
import mysql.connector as sql
from django.db import connection
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import davies_bouldin_score
import matplotlib.pyplot as plt
import base64, urllib
from io import BytesIO

db_connection = sql.connect(database='kitabisa', host = 'localhost', user = 'root', password='Bismillah2203')
atribut_kondisi_rumah = ['luas_bangunan','luas_lahan']
atribut_aset = ['gas','kulkas','ac', 'pemanas_air','telepon_rumah','tv','perhiasan','komputer','sepeda',
               'motor','mobil','perahu','motor_tempel','perahu_motor','kapal','lahan','sapi','kerbau','kuda','babi','kambing','unggas']
atribut = []
for i in atribut_kondisi_rumah :
    atribut.append(i)
for i in atribut_aset :
    atribut.append(i)

def index(request):
    row_count = Rumah.objects.all().count()
    atribut_count = (len(atribut_kondisi_rumah)+len(atribut_aset))
    db_connection = sql.connect(database='kitabisa', host = 'localhost', user = 'root', password='fikkaps21')
    df_kondisi_rumah = pd.read_sql('SELECT * FROM dtks_kondisi_rumah', con=db_connection)
    df_aset = pd.read_sql('SELECT * FROM dtks_aset', con=db_connection)
    
    desc = []
    for i in atribut_kondisi_rumah :
        max_data = df_kondisi_rumah[i].max()
        min_data = df_kondisi_rumah[i].min()
        mean_data = df_kondisi_rumah[i].mean()
        std_data = df_kondisi_rumah[i].std()
        count_data = df_kondisi_rumah[i].count()
        desc.append({'nama' : i, 'max' : max_data, 'min' : min_data, 'mean' : std_data, 'std' : mean_data, 'count' : count_data})
    
    for i in atribut_aset :
        max_data = df_aset[i].max()
        min_data = df_aset[i].min()
        mean_data = df_aset[i].mean()
        std_data = df_aset[i].std()
        count_data = df_aset[i].count()
        desc.append({'nama' : i, 'max' : max_data, 'min' : min_data, 'mean' : std_data, 'std' : mean_data, 'count' : count_data})
    
    context = {
        'row_count' : row_count,
        'atribut_count' : atribut_count,
        'desc'     : desc
    }
    return render(request, 'clustering/index.html', context) 

def proses(request):
    label = ['IDJTG']
    if request.method=="POST":
        name_table = request.POST.get('nama_cl')
        jum_cluster = request.POST.get('klaster')
        for check_atr in atribut :
            check_atr = request.POST.get(check_atr)
        data_cluster = Jenis(
            nama_cluster = name_table,
            jumlah_k = jum_cluster,
            luas_bangunan = request.POST.get('luas_bangunan'),
            luas_lahan = request.POST.get('luas_lahan'),
            gas = request.POST.get('gas'),
            kulkas = request.POST.get('kulkas'),
            ac = request.POST.get('ac'),
            pemanas_air = request.POST.get('pemanas_air'),
            telepon_rumah = request.POST.get('telepon_rumah'),
            tv = request.POST.get('tv'),
            perhiasan = request.POST.get('perhiasan'),
            komputer = request.POST.get('komputer'),
            sepeda = request.POST.get('sepeda'),
            motor = request.POST.get('motor'),
            mobil = request.POST.get('mobil'),
            perahu = request.POST.get('perahu'),
            motor_tempel = request.POST.get('motor_tempel'),
            perahu_motor = request.POST.get('perahu_motor'),
            kapal = request.POST.get('kapal'),
            lahan = request.POST.get('lahan'),
            sapi = request.POST.get('sapi'),
            kerbau = request.POST.get('kerbau'),
            kuda = request.POST.get('kuda'),
            babi = request.POST.get('babi'),
            kambing = request.POST.get('kambing'),
            unggas = request.POST.get('unggas'),
            
        )
        data_cluster.save()
        atr_kondisi = []
        atr_aset = []
        cursor=connection.cursor()
        cursor.execute("CREATE TABLE clustering_"+name_table+"(cluster varchar(100) DEFAULT NULL, IDJTG varchar(100));")
        for check_atr in atribut_kondisi_rumah :
            if (request.POST.get(check_atr) != None):
                atr_kondisi.append(check_atr)
                cursor.execute("ALTER TABLE clustering_"+name_table+" ADD "+check_atr+" INT;")
        for check_atr in atribut_aset :
            if (request.POST.get(check_atr) != None):
                atr_aset.append(check_atr)
                cursor.execute("ALTER TABLE clustering_"+name_table+" ADD "+check_atr+" INT;")
        idjtg = Rumah.objects.values_list("IDJTG", flat=True)
        data_dtks = []
        
        for i in idjtg :
            value = (0,i,)
            for k in atr_kondisi:
                data_rumah = Rumah.objects.get(IDJTG=i)
                a = Kondisi_Rumah.objects.values_list(k, flat=True).get(rumah=data_rumah)
                value = value+(a,)
            for s in atr_aset:
                data_rumah = Rumah.objects.get(IDJTG=i)
                b = Aset.objects.values_list(s, flat=True).get(rumah=data_rumah)
                value = value+(b,)
            data_dtks.append(value)
        values = ', '.join(map(str, data_dtks))
        sql = "INSERT INTO clustering_"+name_table+" VALUES {}".format(values)
        cursor.execute(sql)
              
        return HttpResponseRedirect(reverse('clustering:proses_cluster',args=(name_table,)))
    
    context ={
        'atribut' : atribut
    }
    return render(request, 'clustering/proses.html',context)

def prepocessing(df):
    if ('luas_lahan' in df.columns):
        mean_lahan  = df['luas_lahan'].mean()
        std_lahan = df['luas_lahan'].std()
        limit_atas_lahan = mean_lahan+3*std_lahan
        df = df[(df['luas_lahan'] < limit_atas_lahan)]
        scaler = StandardScaler()
        scaler.fit(df)
        df_scaled = scaler.transform(df)
        df_scaled = pd.DataFrame(df_scaled)
        return df_scaled
    
    else :
        scaler = StandardScaler()
        scaler.fit(df)
        df_scaled = scaler.transform(df)
        df_scaled = pd.DataFrame(df_scaled)
        
        return df_scaled

def proses_cluster(request, name):
    data_cluster = Jenis.objects.get(nama_cluster=name)
    atribut = ['luas_bangunan','luas_lahan','gas','kulkas','ac', 'pemanas_air','telepon_rumah','tv','perhiasan','komputer','sepeda',
               'motor','mobil','perahu','motor_tempel','perahu_motor','kapal','lahan','sapi','kerbau','kuda','babi','kambing','unggas']
    value = []
    variable = []
    for atr in atribut :
        value_list = Jenis.objects.values_list(atr, flat=True).get(nama_cluster=name)
        value.append({'val' : value_list, 'name' : atr})
        if value_list == True :
            variable.append(atr)
       
    test = []
    db_connection = sql.connect(database='kitabisa', host = 'localhost', user = 'root', password='fikkaps21')
    df = pd.read_sql('SELECT * FROM clustering_'+name, con=db_connection)
    df_scaled = prepocessing(df[variable])
    kmeans = KMeans(n_clusters=data_cluster.jumlah_k, random_state=30)
    y_predict = kmeans.fit_predict(df_scaled)
    
    df['cluster'] = y_predict

    df2 = df[df.cluster==0]
    df3 = df[df.cluster==1]
    df4 = df[df.cluster==2]
    plt.switch_backend('agg')
    plt.scatter(df2['luas_bangunan'],df2['luas_lahan'],color='green')
    plt.scatter(df3['luas_bangunan'],df3['luas_lahan'],color='red')
    plt.scatter(df4['luas_bangunan'],df4['luas_lahan'],color='black')

    plt.xlabel('luas_bangunan')
    plt.ylabel('luas_lahan')
    graph = get_graph()
    
    output = []
    cols = []
    for i in df.columns :
        cols.append(i)
    
    for index, row in df.iterrows():
        output.append(row.values)
        test.append({"x" : row['luas_bangunan'], "y" : row["luas_lahan"]})
        cursor=connection.cursor()
        cursor.execute("UPDATE clustering_"+name+" SET cluster="+str(row["cluster"])+" WHERE IDJTG="+str(row["IDJTG"])+";")
        connection.commit()
    print(output)
    
         
    context = {
        "data_cluster" : data_cluster,
        "atribut"   :   atribut, 
        "value"     : value,
        "output"    : output,
        "cols"      : cols,
        "test"      : test,
        "data"      : graph
    }
    return render(request, 'clustering/proses.html', context)

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
    
def analisis_cluster(request):
    get = []
    value = []
    if request.method=="POST":
        for check_atr in atribut_kondisi_rumah :
            if (request.POST.get(check_atr) != None):
                get.append("dtks_kondisi_rumah."+check_atr)
                value.append(check_atr)
                
        for check_atr in atribut_aset :
            if (request.POST.get(check_atr) != None):
                get.append("dtks_aset."+check_atr)
                value.append(check_atr)

    
        sql = "SELECT {}".format(", ".join(str(i) for i in get))+" FROM dtks_kondisi_rumah, dtks_aset WHERE dtks_kondisi_rumah.rumah_id = dtks_aset.rumah_id"
        df = pd.read_sql(sql, con=db_connection)
        df_ = prepocessing(df)
    
        dbi_ = dbi(df_)
        sse_ = sse(df_)
        
        context ={
            'dbi'   : dbi_,
            'sse'   : sse_,
            'value'   : value,
            'atribut' : atribut,

        }
        return render(request, 'clustering/jumlah_k.html',context)    
    
    context = {
        'atribut' : atribut,
        
    }
    return render(request, 'clustering/jumlah_k.html',context)

def dbi(df):
    dbi = []
    index = range(2,10)
    for i in index:
        kmeans = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=100, random_state=42)
        labels = kmeans.fit_predict(df)
        db_index = davies_bouldin_score(df, labels)
        dbi.append({"index" : i, "dbi" : db_index})
    return dbi

def sse(df):
    sse = []
    index = range(2,10)
    for i in index:
        kmeans = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=100, random_state=0)
        kmeans.fit(df)
        sse_ = kmeans.inertia_
        sse.append({"index" : i, "sse" : sse_})
    return sse

def hasil(request):
    clustering = Jenis.objects.all()
    
    context = {
        "cluster"   : clustering
    }
    return render(request, 'clustering/hasil.html', context) 


