from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView 

from inicio.models import Paleta

def inicio(request):
    return render(request, 'inicio/inicio.html')

def sobre_mi(request):
    return render(request, 'inicio/sobre_mi.html')


class PaletaListView(ListView):
    model = Paleta
    template_name = "inicio/lista_paletas.html"


class PaletaDetailView(DetailView):
    model = Paleta
    template_name = "inicio/detalle_paleta.html"


class PaletaCreateView(CreateView):
    model = Paleta
    template_name = "inicio/crear_paleta.html"
    fields = ['modelo','marca','descripcion','stock','fecha_de_carga']
    success_url = '/paletas/'


class PaletaUpdateView(UpdateView):
    model = Paleta
    template_name = "inicio/modificar_paleta.html"
    fields = ['modelo','marca','descripcion','stock','fecha_de_carga']
    success_url = '/paletas/'


class PaletaDeleteView(DeleteView):
    model = Paleta
    template_name = "inicio/eliminar_paleta.html"
    success_url = '/paletas/'
