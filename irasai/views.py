from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views import generic
from django.db.models import Q

from .models import Artistas, Irasas, Katalogas


def index(request):
    num_irasai = Irasas.objects.all().count()
    num_artistai = Artistas.objects.count()
    num_katalogai = Katalogas.objects.all().count()

    context_t = {
        'num_irasai_t': num_irasai,
        'num_artistai_t': num_artistai,
        'num_katalogai_t': num_katalogai,
    }

    return render(request, 'index.html', context=context_t)


def artistai(request):
    artistai_visos_eilutes = Artistas.objects.all()
    # print(authors)
    context_t = {
        'artistai_visos_eilutes_t': artistai_visos_eilutes
    }
    return render(request, 'artistai_visi.html', context=context_t)


def artistas(request, artistas_id):
    artistas_viena_eilute = get_object_or_404(Artistas, pk=artistas_id)
    context_t = {
        'artistas_viena_eilute_t': artistas_viena_eilute
    }
    return render(request, 'artistas_vienas.html', context=context_t)


### klasės tipo views
# generic.ListView - klasė skirta VISŲ eilučių atvaizdavimui
class IrasasListView(generic.ListView): # ListView - visos eilutės (objektai)
    model = Irasas # modelioklasė_list -> book_list
    context_object_name = 'irasas_list'
    template_name = 'irasai_visi.html'


# generic.DetailView - klasė skirta VIENOS eilutės atvaizdavimui
class IrasasDetailView(generic.DetailView):
    model = Irasas
    context_object_name = 'irasas'
    template_name = 'irasas_vienas.html'

class KatalogasListView(generic.ListView): # ListView - visos eilutės (objektai)
    model = Katalogas # modelioklasė_list -> book_list
    context_object_name = 'katalogas_list'
    template_name = 'katalogai_visi.html'


# generic.DetailView - klasė skirta VIENOS eilutės atvaizdavimui
class KatalogasDetailView(generic.DetailView):
    model = Katalogas
    context_object_name = 'katalogas'
    template_name = 'katalogas_vienas.html'

#paieskos viewsas
def search(request):
    paieskos_tekstas = request.GET.get('laukelio-tekstas')
    paieskos_rezultatai = Irasas.objects.filter(
        Q(albumas__icontains = paieskos_tekstas) |
        Q(artistasFK__pavadinimas__icontains = paieskos_tekstas)
    )

    context_t = {
        'paieskos_tekstas_t': paieskos_tekstas,
        'paieskos_rezultatai_t': paieskos_rezultatai
    }
    return render(request, 'paieskos-rezultatai.html', context = context_t)

def searc(request):
    paiesk_tekstas = request.GET.get('laukeli-tekstas')
    paiesk_rezultatai = Irasas.objects.filter(
        Q(aprasymas__icontains = paiesk_tekstas) |
        Q(artistasFK__biografija__icontains = paiesk_tekstas)
    )

    context_t = {
        'paiesk_tekstas_t': paiesk_tekstas,
        'paiesk_rezultatai_t': paiesk_rezultatai
    }
    return render(request, 'paiesk-rezultatai.html', context = context_t)