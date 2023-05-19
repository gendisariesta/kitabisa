from django.shortcuts import render, redirect
from django.http import HttpResponse
from .resources import PenerimaResource
from penerima.models import Penerima
from exportdata.filters import PenerimaFilter



def index(request):
    # penerima_filter=PenerimaFilter(request.POST, queryset=Penerima.objects.all())
    context={
        'title':'Export Data',
        'form':penerima_filter.form,
    }
    return render(request, 'exportdata/index.html', context)

def export(request):
    penerima_resource = PenerimaResource()
    # penerima_filter=PenerimaFilter(request.POST, queryset=Penerima.objects.all())
    # queryset=penerima_filter.qs
    queryset = Penerima.objects.filter(bansos__nama_bansos__contains='Sembako Disabilitas')
    dataset = penerima_resource.export(queryset)
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="penerima.xls"'
    return response
    # dataset = penerima_resource.export()
    # response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    # response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    # return response
