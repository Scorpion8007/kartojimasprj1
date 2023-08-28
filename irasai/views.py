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