from django.db import models
from dtks.models import Bansos

class Kriteria(models.Model):
    ATRIBUT = [
        ('Benefit', 'Benefit'),
        ('Cost', 'Cost'),
    ]
    nama_kriteria = models.CharField(max_length=50, blank=True, null=True)
    bobot = models.IntegerField(blank=True, null=True)
    atribut = models.CharField(max_length=30, choices=ATRIBUT)
<<<<<<< HEAD
    def __str__(self):
        return "{}".format(self.nama_kriteria)
=======
    bansos = models.ForeignKey(Bansos, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return "{}".format(self.nama_kriteria)
    
>>>>>>> 961d98c5e0cd14f35c069bfaebbce432563db7a1
class Crips(models.Model):
    kriteria = models.ForeignKey(Kriteria, on_delete=models.CASCADE)
    nama_crips=models.CharField(max_length=50, blank=True, null=True)
    bobot_crips=models.IntegerField(blank=True, null=True)
<<<<<<< HEAD
    def __str__(self):
        return "{}".format(self.nama_crips)
=======
    bansos = models.ForeignKey(Bansos, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return "{}".format(self.kriteria)
>>>>>>> 961d98c5e0cd14f35c069bfaebbce432563db7a1

