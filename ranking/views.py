# Create your views here.
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.conf.urls.static import static
from dtks.models import Rumah, Aset, Kondisi_Rumah, Anggota, Bansos
from penerima.models import Penerima, Ranking
from .models import Kriteria, Crips
from django.http import HttpResponseRedirect
from datetime import datetime

def index(request,slug,tahun):
    kriteria1 = [f.name for f in Kondisi_Rumah._meta.get_fields()]
    kriteria2 = [f.name for f in Anggota._meta.get_fields()]
    nama_kriteria = kriteria1+kriteria2
    bansos = Bansos.objects.all()
    penerima = Penerima.objects.filter(bansos__slug__contains=slug)
    get_bansos = Bansos.objects.get(slug=slug)
    kriteria = Kriteria.objects.filter(bansos=get_bansos)
    nama_k = Kriteria.objects.values_list('nama_kriteria', flat=True).filter(bansos=get_bansos)
    get_kriteria = ['nama_art']
    for k in nama_k:
        get_kriteria.append(k)
    if request.method == 'POST':
        nama = request.POST.get('nama_kriteria')
        bobot = request.POST.get('bobot')
        atribut = request.POST.get('atribut')
        new_kriteria = Kriteria(nama_kriteria=nama,bobot=bobot,atribut=atribut,bansos=get_bansos)
        new_kriteria.save()
        crips = globals()[nama] 
        for c in crips :
            new_crips = Crips(kriteria = new_kriteria,nama_crips = c,bobot_crips = 0,bansos=get_bansos)
            new_crips.save()
    data_crips = Crips.objects.all()
    data_normalisasi = []
    data_normalisasi1 = []
    data_hasil = []
    anggota = Anggota.objects.all()
    #PROSES NORMALISASI
    for a in anggota:
        nama=a.nama_art
        rumah = a.rumah
        nilai_akhir=[]
        
        data_kriteria = {'nama_art':nama}
        data_kriteria1 = {'nama_art':nama}
        data_hitung = {'nama_art':nama}
        data_normalisasi.append(data_kriteria)
        data_normalisasi1.append(data_kriteria1)
        for c in nama_k:
            kondisi=Kondisi_Rumah.objects.values_list(c, flat=True).get(rumah=rumah)
            bobot = Crips.objects.get(nama_crips=kondisi,bansos=get_bansos).bobot_crips
            bobot_kriteria = Kriteria.objects.get(nama_kriteria=c,bansos=get_bansos).bobot
            value = kondisi
            new = value.replace(value, str(bobot))
            data_kriteria.update({c:new})
            
            atribut = Kriteria.objects.get(nama_kriteria=c).atribut
            k = Kriteria.objects.get(nama_kriteria=c)
            MAX = max(Crips.objects.values_list('bobot_crips', flat=True).filter(kriteria=k))
            MIN = min(Crips.objects.values_list('bobot_crips', flat=True).filter(kriteria=k))
            if bobot != None:
                MAX=1
                MIN=1
                if atribut == "Benefit":
                    norm = int(new)/MAX
                    data_kriteria1.update({c:norm})
                    nilai = norm*bobot_kriteria/100
                    data_hitung.update({c:nilai})
                    nilai_akhir.append(nilai)
                elif atribut == "Cost":
                    norm = MIN/int(new)
                    data_kriteria1.update({c:norm})
                    nilai = norm*bobot_kriteria/100
                    data_hitung.update({c:nilai})
                    nilai_akhir.append(nilai)
                
        data_hitung.update({'nilai_akhir':sum(nilai_akhir)})
        data_hasil.append(data_hitung)
    cek_ranking = Ranking.objects.filter(bansos=get_bansos)
    if not cek_ranking:        
        for d in data_hasil:
            nama = d.get('nama_art')
            anggota = Anggota.objects.get(nama_art=nama)
            hasil = d.get('nilai_akhir')
            data_ranking=Ranking(anggota = anggota,
                                status="Belum Diverifikasi",
                                tahun=datetime.now().year,
                                bansos=get_bansos,
                                alasan="",
                                nilai=hasil)
            data_ranking.save()

    context = {
        'bansos':bansos,
        'slug' : slug,
        'penerima':penerima,
        'kriteria':kriteria,
        'nama_kriteria':nama_kriteria,
        'data_crips' : data_crips,
        'data_normalisasi':data_normalisasi,
        'data_normalisasi1':data_normalisasi1,
        'data_hasil':data_hasil,
        'get_kriteria':get_kriteria
    }
    return render(request, 'ranking/index.html', context) 

def delete_kriteria(request,slug,id):
    Kriteria.objects.get(id=id).delete()
    return redirect ('ranking:index',slug=slug, tahun = datetime.now().year)

def update_kriteria(request,slug,id):
    data_kriteria = Kriteria.objects.get(id=id)
    return redirect ('ranking:index',slug=slug, tahun = datetime.now().year)

def edit_bobot(request,slug,id):
    data_crips = Crips.objects.filter(kriteria=id)
    print (data_crips)
    if request.method == "POST":
        for c in data_crips:
            c.bobot_crips = request.POST['bobot_'+c.nama_crips]
            c.save()
    return redirect ('ranking:index',slug=slug, tahun = datetime.now().year)


status_bangunan = ['Milik sendiri', 'Kontrak/sewa', 'Bebas sewa', 'Dinas', 'Lainnya']
status_lahan = ['Milik sendiri', 'Kontrak/sewa', 'Bebas sewa', 'Dinas', 'Lainnya']
jenis_lantai = ['Marmer/Granit', 'Kramik', 'Parkel/vinil/karpet', 'Ubin/tegel/teraso', 'Kayu/papan kualitas tinggi', 'Semen/bata merah', 'Bambu', 'Kayu/papan berkualitas rendah', 'Tanah', 'Lainnya']
jenis_dinding = ['Tembok', 'Plesteran anyaman bambu/kawat', 'Kayu/papan/gipsum/grc/kalcibot', 'Plesteran anyaman bambu', 'Batang kayu', 'Bambu', 'Lainnya']
kondisi_dinding = ['Bagus / Kualitas Tinggi', 'Jelek / Kualitas rendah']
jenis_atap = ['Beton/genteng beton', 'Genteng keramik', 'Genteng metal', 'Genteng tanah liat', 'Asbes', 'Seng', 'Sirap', 'Bambu', 'Jerami/ijuk/daun/rumbia', 'Lainnya']
kondisi_atap = ['Bagus / Kualitas Tinggi', 'Jelek / Kualitas rendah']
sumber_air = ['Air kemasan bermerk', 'Air isi ulang', 'ledeng meteran', 'ledeng eceran', 'Sumur bor/pompa', 'Sumur terlindung', 'Sumur tak terlindung', 'Mata air  terlindung', 'Mata air tak terlindung', 'Air sungai/danau/waduk', 'Air Hujan', 'Lainnya']
cara_air = ['Membeli eceran', 'Langganan', 'Tidak membeli']
sumber_penerangan = ['Listrik PLN', 'Listrik NON PLN', 'Bukan Listrik']
daya = ['450 watt', '900 watt', '1300 watt', '2200 watt', '>2200 watt', 'Tanpa Meteran']
status_listrik = ['Milik Sendiri', 'Menumpang tetangga']
bahan_bakar = ['Listrik', 'Gas > 3 kg', 'Gas 3kg', 'Gas kota / bio gas', 'minyak tanah', 'Briket', 'Arang', 'kayu bakar', 'Lainnya']
fasilitas_bab = ['Sendiri', 'Bersama', 'Umum', 'Tidak']
jenis_kloset = ['Leher Angsa', 'Plengsengan', 'Cumplung / cubluk', 'Tidak Pakai']
buang_tinja = ['Tangki', 'SPAR ( Saluran pembungan air limbah )', 'Lubang Tanah', 'Kolam/sawah / sungai/ danau / laut', 'Pantai / tanah lapang / kebun', 'lainnya']
bansos_pusat = ['RTLH', 'Air Bersih', 'Listrik', 'Jamban']
# bansos_provinsi = ['RTLH', 'Air Bersih', 'Listrik', 'Jamban']
# bansos_kota = ['RTLH', 'Air Bersih', 'Listrik', 'Jamban']
# bansos_desa = ['RTLH', 'Air Bersih', 'Listrik', 'Jamban']
# bansos_lainnya = ['RTLH', 'Air Bersih', 'Listrik', 'Jamban']

hubungan_krt = ['Kepala Rumah Tangga', 'Istri / suami', 'Anak', 'Menantu', 'Cucu', 'Orang tua / mertua', 'Pembantu / sopir', 'Lainnya']
hubungan_kk = ['Kepala keluarga', 'Istri / suami', 'Anak', 'Menantu', 'Cucu', 'Orang tua / mertua', 'Pembantu / sopir', 'Lainnya']
jenis_kelamin = ['Perempuan', 'Laki-Laki']
status_perkawinan = ['Belum kawin', 'Kawin / nikah', 'Cerai hidup', 'Cerai mati']
akta_nikah = ['Tidak', 'Ya, dapat ditunjukkan', 'Ya, tidak dapat ditunjukkan']
tercantum_kk = ['Ya', 'Tidak']
kepemilikan_kartu = ['Tidak Memiliki', 'Akta Kelahiran', 'Kartu Pelajar', 'KTP', 'SIM']
status_kehamilan = ['Ya', 'Tidak']
jenis_disabilitas = ['Tidak disabilitas', 'Disabilitas fisik', 'Disabilitas Netra / Buta', 'Disabilitas rungu', 'Disabilitas wicara', 'Disabilitas wicara dan rungu', 'Disabilitas netra dan disabilitas fisik', 'Disabilitas Netra, Rungu dan Wicara', 'Disabilitas Rungu, Wicara, Fisik', 'Disabilitas Rungu, Wicara, Netra, Fisik', 'Disabilitas Intelektual', 'Disabilitas mental ( Gangguan Jiwa )', 'Disabilitas Fisik dan mental ( gangguan jiwa )', 'Mantan Penderita gangguan jiwa', 'Disabilitas mental ( Gangguan Jiwa ) dan Intelektual', 'Disabilitas Fisik dan mental ( gangguan jiwa ) dan Intelektual']
penyakit = ['Tidak ada', 'Hipertensi ( Tekanan darah tinggi )', 'Rematik', 'Asma', 'Masalah jantung', 'Diabetes ( Kencing manis )', 'Tuberculosis ( TBC )', 'Stroke', 'Kanker atau Tumor Ganas', 'Lainnya ( Gagal ginjal, paru - paru, flek dan sejenisnya )']
sekolah = ['Tidak / belum sekolah', 'Masih sekolah', 'Tidak sekolah lagi']
jenjang_pendidikan = ['Tidak sekolah', 'SD / SDLB', 'Paket A', 'M. Ibtidiyah', 'ULA ( Pesantren setara SD )', 'SMP / SMPLB', 'Paket B', 'M. Tsanawiyah', 'Wustha ( Pesantren setara SMP )', 'SMA / SMK / SMALB', 'Paket C', 'M. Aliyah', 'Ulya ( Pesantren setra SMA )', 'Perguruan Tinggi']
status_bekerja = ['Bekerja', 'Tidak Bekerja']
status_kedudukan_kerja = ['Tidak bekerja', 'Berusaha sendiri', 'Berusaha dibantu buruh tidak tetap / tidak dibayar', 'Berusaha dibantu buruh tetap / dibayar', 'Buruh / Karyawan / Pegawai swasta', 'PNS / TNI / POLRI / BUMN / BUMD / Anggota Legislatif', 'Pekerja bebas pertanian', 'Pekerja bebas Non Pertanian', 'Pekerja keluarga / tidak dibayar']
bansos_provinsi = ['KJS', 'KUBE', 'PBI Pemda Provinsi']
bansos_kota = ['PBI Kab Kota', 'Lainnya']
bansos_desa = ['Dana Desa', 'Lainnya']
bansos_lainnya =['KUR', 'BPJS Mandiri', 'Asuransi kesehatan', 'BPJS Ketenagakerjaan', 'BPJS PPU', 'Lainnya']
