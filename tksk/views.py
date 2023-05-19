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
    data_rumah = Rumah.objects.all()
    data_aset = Aset.objects.all()
    context={
        'title': 'Input Data',
        'data_rumah': data_rumah,
        'data_aset': data_aset
    }
    return render (request, 'tksk/input.html', context)

def input_krt(request):
    data_kecamatan = Kecamatan.objects.all()
    context={
        'title': 'Input Form DTKS',
        'data_kecamatan' : data_kecamatan
    }
    if request.method == 'POST':
        idjtg = request.POST['IDJTG']
        nama_krt = request.POST['nama_krt']
        kabupaten = request.POST['kabupaten']
        id_kecamatan = request.POST.get('kecamatan')
        kecamatan = Kecamatan.objects.get(id=id_kecamatan)
        desa = request.POST['desa']
        dusun = request.POST['dusun']
        rt = request.POST['rt']
        rw = request.POST['rw']
        alamat = request.POST['alamat']
        koordinat_lat = request.POST['koordinat_lat']
        koordinat_long = request.POST['koordinat_long']
        if koordinat_lat=="" and koordinat_long=="":
            koordinat_lat=None
            koordinat_long=None
        data_rumah = Rumah(IDJTG=idjtg,nama_krt=nama_krt,kabupaten=kabupaten,kecamatan=kecamatan,desa=desa,dusun=dusun,rt=rt,rw=rw,alamat=alamat,koordinat_lat = koordinat_lat,koordinat_long = koordinat_long)
        data_rumah.save()
        
        gas = request.POST['gas']
        kulkas = request.POST['kulkas']
        ac = request.POST['ac']
        pemanas_air = request.POST['pemanas_air']
        telepon_rumah = request.POST['telepon_rumah']
        tv = request.POST['tv']
        perhiasan = request.POST['perhiasan']
        komputer = request.POST['komputer']
        sepeda = request.POST['sepeda']
        motor = request.POST['motor']
        mobil = request.POST['mobil']
        perahu = request.POST['perahu']
        motor_tempel = request.POST['motor_tempel']
        perahu_motor = request.POST['perahu_motor']
        kapal = request.POST['kapal']
        lahan = request.POST['lahan']
        rumah_lain = request.POST['rumah_lain']
        sapi = request.POST['sapi']
        kerbau = request.POST['kerbau']
        kuda = request.POST['kuda']
        babi = request.POST['babi']
        kambing = request.POST['kambing']
        unggas = request.POST['unggas']
        pengeluaran = request.POST['pengeluaran']
        data_aset = Aset(
        rumah=data_rumah,
        gas=gas,
        kulkas=kulkas,
        ac=ac,
        pemanas_air=pemanas_air,
        telepon_rumah=telepon_rumah,
        tv=tv,
        perhiasan=perhiasan,
        komputer = komputer,
        sepeda = sepeda,
        motor = motor,
        mobil = mobil,
        perahu = perahu,
        motor_tempel = motor_tempel,
        perahu_motor = perahu_motor,
        kapal = kapal,
        lahan = lahan,
        rumah_lain = rumah_lain,
        sapi = sapi,
        kerbau = kerbau,
        kuda = kuda,
        babi = babi,
        kambing = kambing,
        unggas = unggas,
        pengeluaran = pengeluaran)
        data_aset.save()
        
        status_bangunan = request.POST['status_bangunan']
        luas_bangunan = request.POST['luas_bangunan']
        status_lahan = request.POST['status_lahan']
        luas_lahan = request.POST['luas_lahan']
        luas_lantai = request.POST['luas_lantai']
        jenis_lantai = request.POST['jenis_lantai']
        jenis_dinding = request.POST['jenis_dinding']
        kondisi_dinding = request.POST['kondisi_dinding']
        jenis_atap = request.POST['jenis_atap']
        kondisi_atap = request.POST['kondisi_atap']
        jum_kamar = request.POST['jum_kamar']
        sumber_air = request.POST['sumber_air']
        cara_air = request.POST['cara_air']
        sumber_penerangan = request.POST['sumber_penerangan']
        daya = request.POST['daya']
        id_pel = request.POST['id_pel']
        status_listrik = request.POST['status_listrik']
        bahan_bakar = request.POST['bahan_bakar']
        fasilitas_bab = request.POST['fasilitas_bab']
        jenis_kloset = request.POST['jenis_kloset']
        buang_tinja = request.POST['buang_tinja']
        bansos_pusat = request.POST.get('bansos_pusat', False)
        bansos_provinsi = request.POST.get('bansos_provinsi', False)
        bansos_kota = request.POST.get('bansos_kabupaten', False)
        bansos_desa = request.POST.get('bansos_desa', False)
        bansos_lainnya = request.POST.get('bansos_lainnya', False)
        sumber_bansos = request.POST.get('sumber_bansos')
        data_kondisi = Kondisi_Rumah(
        rumah=data_rumah, 
        status_bangunan = status_bangunan,
        luas_bangunan = luas_bangunan,
        status_lahan = status_lahan,
        luas_lahan = luas_lahan,
        luas_lantai = luas_lantai,
        jenis_lantai = jenis_lantai,
        jenis_dinding = jenis_dinding,
        kondisi_dinding = kondisi_dinding,
        jenis_atap = jenis_atap,
        kondisi_atap = kondisi_atap,
        jum_kamar = jum_kamar,
        sumber_air = sumber_air,
        cara_air = cara_air,
        sumber_penerangan = sumber_penerangan,
        daya = daya,
        id_pel = id_pel,
        status_listrik = status_listrik,
        bahan_bakar = bahan_bakar,
        fasilitas_bab = fasilitas_bab,
        jenis_kloset = jenis_kloset,
        buang_tinja = buang_tinja,
        bansos_pusat = bansos_pusat,
        bansos_provinsi = bansos_provinsi,
        bansos_kota = bansos_kota,
        bansos_desa = bansos_desa,
        bansos_lainnya = bansos_lainnya,
        sumber_bansos = sumber_bansos,
        )
        data_kondisi.save()
        id = data_rumah.id
        return HttpResponseRedirect(reverse('tksk:detailkrt',args=(id,)))
    return render (request, 'tksk/input_krt.html', context)

def detailkrt(request, id):
  data_rumah = Rumah.objects.get(id=id)
  id_rumah = data_rumah.id
  data_aset = Aset.objects.get(rumah=id_rumah)
  data_kondisi = Kondisi_Rumah.objects.get(rumah=id_rumah)
  data_anggota = Anggota.objects.filter(rumah=id_rumah)
  context={
    'data_rumah'    : data_rumah,
    'data_aset'     : data_aset,
    'data_kondisi'  : data_kondisi,
    'data_anggota'  : data_anggota,
  }
  return render(request, 'tksk/detail_krt.html', context)

def detailart(request, id):
  data_anggota = Anggota.objects.get(id=id)
  id_rumah = data_anggota.rumah_id
  context={
    'data_anggota' : data_anggota,
    'id_rumah'  : id_rumah
  }
  return render(request, 'tksk/detail_art.html', context)

def input_art(request, id):
  data_rumah = Rumah.objects.get(id=id)
  id = data_rumah.id
  
  if request.method == 'POST':
    idjtg_art = request.POST['idjtg_art']
    nama_art = request.POST['nama_art']
    nik = request.POST['nik']
    no_kk = request.POST['no_kk']
    ibu_kandung = request.POST['ibu_kandung']
    hubungan_krt = request.POST['hubungan_krt']
    hubungan_kk = request.POST['hubungan_kk']
    tempat_lahir = request.POST['tempat_lahir']
    tanggal_lahir = request.POST['tanggal_lahir']
    jenis_kelamin = request.POST['jenis_kelamin']
    status_perkawinan = request.POST['status_perkawinan']
    akta_nikah = request.POST['akta_nikah']
    tercantum_kk = request.POST['tercantum_kk']
    kepemilikan_kartu = request.POST['kepemilikan_kartu']
    status_kehamilan = request.POST['status_kehamilan']
    tgl_kehamilan = request.POST['tgl_kehamilan']
    jenis_disabilitas = request.POST['jenis_disabilitas']
    penyakit = request.POST['penyakit']
    sekolah = request.POST['sekolah']
    jenjang_pendidikan = request.POST['jenjang_pendidikan']
    kelas_tertinggi = request.POST['kelas_tertinggi']
    ijazah_tertinggi = request.POST['ijazah_tertinggi']
    status_bekerja = request.POST['status_bekerja']
    lapangan_usaha = request.POST['lapangan_usaha']
    status_kedudukan_kerja = request.POST['status_kedudukan_kerja']
    jenis_ketrampilan = request.POST['jenis_ketrampilan']
    # bansos_pusat = request.POST['bansos_pusat']
    bansos_provinsi = request.POST['bansos_provinsi']
    bansos_kota = request.POST['bansos_kabupaten']
    bansos_desa = request.POST['bansos_desa']
    bansos_lainnya = request.POST['bansos_lainnya']
    data_anggota = Anggota(
      IDJTG_ART = idjtg_art,
      rumah = data_rumah,
      nama_art = nama_art,
      nik = nik,
      no_kk = no_kk,
      ibu_kandung = ibu_kandung,
      hubungan_krt = hubungan_krt,
      hubungan_kk = hubungan_kk,
      tempat_lahir = tempat_lahir,
      tanggal_lahir = tanggal_lahir,
      jenis_kelamin = jenis_kelamin,
      status_perkawinan = status_perkawinan,
      akta_nikah = akta_nikah,
      tercantum_kk = tercantum_kk,
      kepemilikan_kartu = kepemilikan_kartu,
      status_kehamilan = status_kehamilan,
      tgl_kehamilan = tgl_kehamilan,
      jenis_disabilitas = jenis_disabilitas,
      penyakit = penyakit,
      sekolah = sekolah,
      jenjang_pendidikan = jenjang_pendidikan,
      kelas_tertinggi = kelas_tertinggi,
      ijazah_tertinggi = ijazah_tertinggi,
      status_bekerja = status_bekerja,
      lapangan_usaha = lapangan_usaha,
      status_kedudukan_kerja = status_kedudukan_kerja,
      jenis_ketrampilan = jenis_ketrampilan,
      bansos_pusat = "0",
      bansos_provinsi = bansos_provinsi,
      bansos_kota = bansos_kota,
      bansos_desa = bansos_desa,
      bansos_lainnya = bansos_lainnya
      )
    data_anggota.save()
    return HttpResponseRedirect(reverse('tksk:detailart',args=(id,)))  
  context={
    'data_rumah'  : data_rumah,
    'input_art'    : 'active',
  }
  return render(request, 'tksk/input_art.html', context)
