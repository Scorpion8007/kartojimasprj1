from django.shortcuts import render
from .models import Artistas,Irasas
# Create your views here.

from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views import generic
from django.db.models import Q

def index(request):
    num_irasai = Irasas.objects.all().count()
    num_artistai = Artistas.objects.all().count()

    context_t = {
        'num_irasai_t': num_irasai,
        'num_artistai_t': num_artistai,
    }

    return render(request, 'index.html', context=context_t)

def artistai(request):
    artistai = Artistas.objects.all()
    # print(authors)
    context_t = {
        'artistai_t': artistai
    }
    return render(request, 'artistai_visi.html', context=context_t)

def artistas(request, artistas_id):
    artistas_viena_eilute = get_object_or_404(Artistas, pk=artistas_id)
    context_t = {
        'artistas_t': artistas_viena_eilute
    }
    return render(request, 'artistas_vienas.html', context=context_t)