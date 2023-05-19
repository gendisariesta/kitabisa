from django.contrib import admin
from .models import Penerima

# Register your models here.
class PenerimaAdmin(admin.ModelAdmin):
    list_display = ('anggota', 'bansos', 'tahun')
    

admin.site.register(Penerima, PenerimaAdmin)
