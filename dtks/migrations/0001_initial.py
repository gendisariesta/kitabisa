# Generated by Django 4.1.6 on 2023-05-02 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bansos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_bansos', models.CharField(max_length=50)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('kuota', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kecamatan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kecamatan', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['nama_kecamatan'],
            },
        ),
        migrations.CreateModel(
            name='Rumah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDJTG', models.CharField(max_length=100)),
                ('nama_krt', models.CharField(max_length=100)),
                ('kabupaten', models.CharField(max_length=100)),
                ('desa', models.CharField(max_length=100)),
                ('dusun', models.CharField(max_length=100)),
                ('rt', models.IntegerField()),
                ('rw', models.IntegerField()),
                ('alamat', models.CharField(max_length=150)),
                ('koordinat_lat', models.CharField(blank=True, max_length=100, null=True)),
                ('koordinat_long', models.CharField(blank=True, max_length=100, null=True)),
                ('kecamatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dtks.kecamatan')),
            ],
        ),
        migrations.CreateModel(
            name='Kondisi_Rumah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_bangunan', models.CharField(max_length=100)),
                ('luas_bangunan', models.IntegerField()),
                ('status_lahan', models.CharField(max_length=100)),
                ('luas_lahan', models.IntegerField()),
                ('luas_lantai', models.IntegerField()),
                ('jenis_lantai', models.CharField(max_length=100)),
                ('jenis_dinding', models.CharField(max_length=100)),
                ('kondisi_dinding', models.CharField(max_length=100)),
                ('jenis_atap', models.CharField(max_length=100)),
                ('kondisi_atap', models.CharField(max_length=100)),
                ('jum_kamar', models.IntegerField()),
                ('sumber_air', models.CharField(max_length=100)),
                ('cara_air', models.CharField(max_length=100)),
                ('sumber_penerangan', models.CharField(max_length=100)),
                ('daya', models.CharField(max_length=100)),
                ('id_pel', models.CharField(max_length=150, null=True)),
                ('status_listrik', models.CharField(max_length=100)),
                ('bahan_bakar', models.CharField(max_length=100)),
                ('fasilitas_bab', models.CharField(max_length=100)),
                ('jenis_kloset', models.CharField(max_length=100)),
                ('buang_tinja', models.CharField(max_length=100)),
                ('bansos_pusat', models.CharField(max_length=100, null=True)),
                ('bansos_provinsi', models.CharField(max_length=100, null=True)),
                ('bansos_kota', models.CharField(max_length=100, null=True)),
                ('bansos_desa', models.CharField(max_length=100, null=True)),
                ('bansos_lainnya', models.CharField(max_length=100, null=True)),
                ('sumber_bansos', models.CharField(max_length=100, null=True)),
                ('koordinat_lat', models.CharField(blank=True, max_length=100, null=True)),
                ('koordinat_long', models.CharField(blank=True, max_length=100, null=True)),
                ('rumah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dtks.rumah')),
            ],
            options={
                'ordering': ['luas_lahan'],
            },
        ),
        migrations.CreateModel(
            name='Aset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gas', models.IntegerField(default=0, null=True)),
                ('kulkas', models.IntegerField(default=0, null=True)),
                ('ac', models.IntegerField(default=0, null=True)),
                ('pemanas_air', models.IntegerField(default=0, null=True)),
                ('telepon_rumah', models.IntegerField(default=0, null=True)),
                ('tv', models.IntegerField(default=0, null=True)),
                ('perhiasan', models.IntegerField(default=0, null=True)),
                ('komputer', models.IntegerField(default=0, null=True)),
                ('sepeda', models.IntegerField(default=0, null=True)),
                ('motor', models.IntegerField(default=0, null=True)),
                ('mobil', models.IntegerField(default=0, null=True)),
                ('perahu', models.IntegerField(default=0, null=True)),
                ('motor_tempel', models.IntegerField(default=0, null=True)),
                ('perahu_motor', models.IntegerField(default=0, null=True)),
                ('kapal', models.IntegerField(default=0, null=True)),
                ('lahan', models.IntegerField(default=0, null=True)),
                ('rumah_lain', models.IntegerField(default=0, null=True)),
                ('sapi', models.IntegerField()),
                ('kerbau', models.IntegerField()),
                ('kuda', models.IntegerField()),
                ('babi', models.IntegerField()),
                ('kambing', models.IntegerField()),
                ('unggas', models.IntegerField()),
                ('pengeluaran', models.CharField(max_length=150)),
                ('rumah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dtks.rumah')),
            ],
            options={
                'ordering': ['pengeluaran'],
            },
        ),
        migrations.CreateModel(
            name='Anggota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDJTG_ART', models.CharField(max_length=150)),
                ('nama_art', models.CharField(max_length=255)),
                ('nik', models.CharField(max_length=100)),
                ('no_kk', models.CharField(max_length=100)),
                ('ibu_kandung', models.CharField(max_length=255)),
                ('hubungan_krt', models.CharField(max_length=100)),
                ('hubungan_kk', models.CharField(max_length=100)),
                ('tempat_lahir', models.CharField(max_length=100)),
                ('tanggal_lahir', models.DateField()),
                ('jenis_kelamin', models.CharField(max_length=50)),
                ('status_perkawinan', models.CharField(max_length=100)),
                ('akta_nikah', models.CharField(max_length=100)),
                ('tercantum_kk', models.CharField(max_length=100)),
                ('kepemilikan_kartu', models.CharField(max_length=100)),
                ('status_kehamilan', models.CharField(max_length=100)),
                ('tgl_kehamilan', models.DateField(null=True)),
                ('jenis_disabilitas', models.CharField(max_length=100)),
                ('penyakit', models.CharField(max_length=100)),
                ('sekolah', models.CharField(max_length=100)),
                ('jenjang_pendidikan', models.CharField(default='Tidak sekolah', max_length=100, null=True)),
                ('kelas_tertinggi', models.CharField(default=0, max_length=100, null=True)),
                ('ijazah_tertinggi', models.CharField(default='Tidak punya ijazah', max_length=100, null=True)),
                ('status_bekerja', models.CharField(default='Tidak Bekerja', max_length=100, null=True)),
                ('lapangan_usaha', models.CharField(default='Tidak bekerja', max_length=100, null=True)),
                ('status_kedudukan_kerja', models.CharField(default='Tidak bekerja', max_length=100, null=True)),
                ('jenis_ketrampilan', models.CharField(default='Tidak Ada', max_length=100, null=True)),
                ('bansos_pusat', models.CharField(max_length=100, null=True)),
                ('bansos_provinsi', models.CharField(max_length=100, null=True)),
                ('bansos_kota', models.CharField(max_length=100, null=True)),
                ('bansos_desa', models.CharField(max_length=100, null=True)),
                ('bansos_lainnya', models.CharField(max_length=100, null=True)),
                ('rumah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dtks.rumah')),
            ],
            options={
                'ordering': ['nama_art'],
            },
        ),
    ]
