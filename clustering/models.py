from django.db import models

# Create your models here.
class Jenis(models.Model):
  nama_cluster = models.CharField(max_length=100)
  jumlah_k = models.IntegerField()
  luas_bangunan = models.BooleanField(default=False, null=True)
  luas_lahan = models.BooleanField(default=False, null=True)
  gas = models.BooleanField(default=False, null=True)
  kulkas = models.BooleanField(default=False, null=True)
  ac = models.BooleanField(default=False, null=True)
  pemanas_air = models.BooleanField(default=False, null=True)
  telepon_rumah = models.BooleanField(default=False, null=True)
  tv = models.BooleanField(default=False, null=True)
  perhiasan = models.BooleanField(default=False, null=True)
  komputer = models.BooleanField(default=False, null=True)
  sepeda = models.BooleanField(default=False, null=True)
  motor = models.BooleanField(default=False, null=True)
  mobil = models.BooleanField(default=False, null=True)
  perahu = models.BooleanField(default=False, null=True)
  motor_tempel = models.BooleanField(default=False, null=True)
  perahu_motor = models.BooleanField(default=False, null=True)
  kapal = models.BooleanField(default=False, null=True)
  lahan = models.BooleanField(default=False, null=True)
  sapi = models.BooleanField(default=False, null=True)
  kerbau = models.BooleanField(default=False, null=True)
  kuda = models.BooleanField(default=False, null=True)
  babi = models.BooleanField(default=False, null=True)
  kambing = models.BooleanField(default=False, null=True)
  unggas = models.BooleanField(default=False, null=True)
  
  def __str__(self):
    return "{}".format(self.nama_cluster)