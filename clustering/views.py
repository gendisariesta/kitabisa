# Create your views here.
from django.shortcuts import render, redirect
from dtks.models import Rumah, Aset, Kondisi_Rumah, Bansos
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
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import base64, urllib
from io import BytesIO

from django.contrib.auth.decorators import login_required
from account.decorators import unauthenticated_user, allowed_users

db_connection = sql.connect(database='kitabisa', host = 'localhost', user = 'root', password='fikkaps21')
atribut_kondisi_rumah = ['luas_bangunan','luas_lahan']
atribut_aset = ['gas','kulkas','ac', 'pemanas_air','telepon_rumah','tv','perhiasan','komputer','sepeda',
               'motor','mobil','perahu','motor_tempel','perahu_motor','kapal','lahan','sapi','kerbau','kuda','babi','kambing','unggas']
atribut = []
for i in atribut_kondisi_rumah :
    atribut.append(i)
for i in atribut_aset :
    atribut.append(i)

@login_required(login_url='account:login')
@allowed_users(allowed_roles=['Superadmin', 'Admin'])
def index(request):
    row_count = Rumah.objects.all().count()
    atribut_count = (len(atribut_kondisi_rumah)+len(atribut_aset))
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
    bansos = Bansos.objects.all()
    context = {
        'row_count' : row_count,
        'atribut_count' : atribut_count,
        'desc'     : desc,
        'title':'Clustering',
        'bansos':bansos,
    }
    return render(request, 'clustering/index.html', context) 

def outlier(df):
    mean_lahan  = df['luas_lahan'].mean()
    std_lahan = df['luas_lahan'].std()
    limit_atas_lahan = mean_lahan+3*std_lahan
    df = df[(df['luas_lahan'] < limit_atas_lahan)]
    return df
    
def scaling(df):
    scaler = StandardScaler()
    scaler.fit(df)
    df_scaled = scaler.transform(df)
    df_scaled = pd.DataFrame(df_scaled)
    return df_scaled

@login_required(login_url='account:login')
@allowed_users(allowed_roles=['Superadmin', 'Admin'])
def proses(request):
    global data, name_table, jum_cluster, value, atr_kondisi, atr_aset
    
    if 'proses' in request.POST:
        name_table = request.POST.get('nama_cl')
        jum_cluster = request.POST.get('klaster')

        value = []
        get = []
        query = []
        atr_kondisi = []
        atr_aset = []
        
        for check_atr in atribut_kondisi_rumah :
            if (request.POST.get(check_atr) != None):
                get.append("dtks_kondisi_rumah."+check_atr)
                query.append(check_atr+" INT")
                value.append(check_atr)
                atr_kondisi.append(check_atr)
                
        for check_atr in atribut_aset :
            if (request.POST.get(check_atr) != None):
                get.append("dtks_aset."+check_atr)
                query.append(check_atr+" INT")
                value.append(check_atr)
                atr_aset.append(check_atr)
    
        sql = "SELECT dtks_rumah.IDJTG, {}".format(", ".join(str(i) for i in get))+" FROM dtks_rumah, dtks_kondisi_rumah, dtks_aset WHERE dtks_rumah.id = dtks_kondisi_rumah.rumah_id and dtks_kondisi_rumah.rumah_id = dtks_aset.rumah_id"
        df = pd.read_sql(sql, con=db_connection)
        if ('luas_lahan' in df.columns):
            df = outlier(df)
            df_scaled = scaling(df[value])
            kmeans = KMeans(n_clusters=int(jum_cluster), random_state=30)
            y_predict = kmeans.fit_predict(df_scaled)
            # df['cluster'] = y_predict
            df.insert(loc=0, column='cluster', value=y_predict)
            
            data = df
            output =[]
            for index, row in df.iterrows():
                output.append(row.values)
            
            cols = []
            for i in df.columns :
                cols.append(i)
                            
            df2 = df[df.cluster==0]
            df3 = df[df.cluster==1]
            df4 = df[df.cluster==2]
            plt.switch_backend('agg')
            plt.scatter(df2['cluster'],df2['luas_lahan'],color='green')
            plt.scatter(df3['cluster'],df3['luas_lahan'],color='red')
            plt.scatter(df4['cluster'],df4['luas_lahan'],color='black')

            plt.xlabel('luas_bangunan')
            plt.ylabel('luas_lahan')
            graph = get_graph()
        
        bansos = Bansos.objects.all()   
        context = {
            "output" : output,
            "cols" : cols,
            "atribut"   :   atribut, 
            "value"     : value,
            "data"      : graph,
            "name_table"  : name_table,
            "jum_cluster"   : jum_cluster,
            'bansos':bansos,
            'title':'Clustering',
        }
        return render(request, 'clustering/proses.html', context)
    if 'simpan' in request.POST:
        val_atr = "{}".format(', '.join(value))
        cluster_jenis = Jenis(nama_cluster = name_table, jumlah_k = jum_cluster, atribut = val_atr)
        cluster_jenis.save()
        cursor=connection.cursor()
        cursor.execute("CREATE TABLE clustering_"+name_table+"(cluster varchar(100) DEFAULT NULL, IDJTG varchar(100));")
        for check_atr in value :
            cursor.execute("ALTER TABLE clustering_"+name_table+" ADD "+check_atr+" INT;")
        
        data_dtks = []
        idjtg = data['IDJTG']
        print(idjtg)
        for i in idjtg :
            values = (0,i,)
            for k in atr_kondisi:
                data_rumah = Rumah.objects.get(IDJTG=i)
                a = Kondisi_Rumah.objects.values_list(k, flat=True).get(rumah=data_rumah)
                values = values+(a,)
            for s in atr_aset:
                data_rumah = Rumah.objects.get(IDJTG=i)
                b = Aset.objects.values_list(s, flat=True).get(rumah=data_rumah)
                values = values+(b,)
            data_dtks.append(values)
        values_ = ', '.join(map(str, data_dtks))
        sql = "INSERT INTO clustering_"+name_table+" VALUES {}".format(values_)
        cursor.execute(sql)
        for index, row in data.iterrows():
            cursor.execute("UPDATE clustering_"+name_table+" SET cluster="+str(row["cluster"])+" WHERE IDJTG="+str(row["IDJTG"])+";")
            connection.commit()
        return HttpResponseRedirect(reverse('clustering:c',args=(name_table,)))
    
    bansos = Bansos.objects.all()
    context ={
        'atribut' : atribut,
        'bansos':bansos,
        'title':'Clustering',
    }
    return render(request, 'clustering/proses.html',context)

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def c(request, name):
    nama = name
    db_connection = sql.connect(database='kitabisa', host = 'localhost', user = 'root', password='fikkaps21')
    data = pd.read_sql('SELECT * FROM clustering_'+nama, con=db_connection)
    value = data.columns[2:]
    jum = data['cluster'].nunique()
    output = []
    cols = []
    for i in data.columns :
        cols.append(i)
    for index, row in data.iterrows():
        output.append(row.values) 
    
    df2 = data[(data['cluster'] == 0)]
    df3 = data[(data['cluster'] == 1)]
    df4 = data[(data['cluster'] == 2)]
    
    plt.switch_backend('agg')
    plt.scatter(df2['cluster'],df2['luas_lahan'],color='green')
    plt.scatter(df3['cluster'],df3['luas_lahan'],color='red')
    plt.scatter(df4['cluster'],df4['luas_lahan'],color='black')

    plt.xlabel('luas_bangunan')
    plt.ylabel('luas_lahan')
    graph = get_graph()
    print(output)

    bansos = Bansos.objects.all()
    context = {
        "atribut"   :   atribut, 
        "value"     : value,
        "output"    : output,
        "cols"      : cols,
        "data"      : graph,
        "name_table"    : name,
        "jum_cluster"   : jum,
        "simpan"    : "true",
        'bansos':bansos,
        'title':'Clustering',
    }
    return render(request, 'clustering/proses.html', context)

@login_required(login_url='account:login')
@allowed_users(allowed_roles=['Superadmin', 'Admin'])
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
        if ('luas_lahan' in df.columns):
            df = outlier(df)
            df_ = scaling(df)
            dbi_ = dbi(df_)
            silhouette_ = silhouette(df_)
        else:
            df_ = scaling(df)
            dbi_ = dbi(df_)
            silhouette_ = silhouette(df_)

        bansos = Bansos.objects.all()
        context ={
            'dbi'   : dbi_,
            'silhouette'   : silhouette_,
            'value'   : value,
            'atribut' : atribut,
            'bansos':bansos,
            'title':'Clustering',
        }
        return render(request, 'clustering/jumlah_k.html',context) 
       
    bansos = Bansos.objects.all()
    context = {
        'atribut' : atribut,
        'bansos':bansos,
        'title':'Clustering',
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

def silhouette(df):
    score = []
    index = range(2,10)
    for i in index:
        kmeans = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=100, random_state=42)
        labels = kmeans.fit_predict(df)
        silhouette_avg = silhouette_score(df, labels)
        score.append(({"index" : i, "silhouette" : silhouette_avg}))
    return score

def hasil(request):
    clustering = Jenis.objects.all()
    
    bansos = Bansos.objects.all()
    context = {
        "cluster"   : clustering,
        'bansos':bansos,
        'title':'Clustering',
    }
    return render(request, 'clustering/hasil.html', context) 

def delete(request, name):
  Jenis.objects.get(nama_cluster=name).delete()
  cursor=connection.cursor()
  cursor.execute("DROP TABLE clustering_"+name+";")
  return HttpResponseRedirect('/clustering/hasil')

def dtks(request, idjtg):
    data = Rumah.objects.get(IDJTG = idjtg).id
    
    return HttpResponseRedirect(reverse('dtks:detail',args=(data,)))
    

