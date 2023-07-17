from django.db import models
from dtks.models import Anggota, Kecamatan, Bansos


# Create your models here.
class Penerima(models.Model):
  STATUSES = [
        ('Dalam Proses', 'Dalam Proses'),
        ('Diterima', 'Diterima'),
        ]
  anggota=models.ForeignKey(Anggota, on_delete=models.CASCADE)
  foto_bukti = models.FileField(upload_to='bukti/', null=True)
  tahun = models.CharField(max_length=10, blank=True, null=True)
  bansos = models.ForeignKey(Bansos, on_delete=models.CASCADE, null=True)
  date = models.DateTimeField(auto_now_add=True, blank=True)
  status= models.CharField(max_length=60, choices=STATUSES, default='Dalam Proses')

  def __str__(self):
    return "{}. {}".format(self.id, self.anggota) 


class Ranking(models.Model):
  STATUS_VERIF=[
    ('Belum Diverifikasi', 'Belum Diverifikasi'),
    ('Disetujui', 'Disetujui'),
    ('Ditolak', 'Ditolak'),
    ('Penerima', 'Penerima'),
  ]
  anggota=models.ForeignKey(Anggota, on_delete=models.CASCADE)
  status=models.CharField(max_length=20, choices=STATUS_VERIF, default='Belum Diverifikasi')
  tahun = models.CharField(max_length=10, blank=True, null=True)
  bansos = models.ForeignKey(Bansos, on_delete=models.CASCADE, null=True)
<<<<<<< HEAD
  alasan = models.CharField(max_length=200, blank=True, null=True)
=======
>>>>>>> 961d98c5e0cd14f35c069bfaebbce432563db7a1
  nilai = models.FloatField(blank=True, null=True, default='0')