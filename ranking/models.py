from django.db import models

class Kriteria(models.Model):
    ATRIBUT = [
        ('Benefit', 'Benefit'),
        ('Cost', 'Cost'),
    ]
    nama_kriteria = models.CharField(max_length=50, blank=True, null=True)
    bobot = models.IntegerField(blank=True, null=True)
    atribut = models.CharField(max_length=30, choices=ATRIBUT)
    
class Crips(models.Model):
    kriteria = models.ForeignKey(Kriteria, on_delete=models.CASCADE)
    nama_crips=models.CharField(max_length=50, blank=True, null=True)
    bobot_crips=models.IntegerField(blank=True, null=True)

