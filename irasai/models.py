from django.db import models

import uuid


class Artistas(models.Model):
    pavadinimas = models.CharField('Pavadinimas', max_length=80)
    metai = models.IntegerField('Pradėjo-metai')
    biografija = models.TextField('Bio', max_length=2000)

    def __str__(self):
        return self.pavadinimas


class Irasas(models.Model):
    albumas = models.CharField('Albumas', max_length=100)
    metai_pasirode = models.IntegerField('Pirmo leidimo metai')
    aprasymas = models.TextField('Aprašymas', max_length=2000)
    # related_name='irasas_set', irasas_set bus naudojamas iš Artistas objekto, jo įrašams ištraukti
    artistasFK = models.ForeignKey(Artistas, on_delete=models.SET_NULL, null=True, related_name='irasas_set')

    def __str__(self):
        return self.albumas

class Katalogas(models.Model):
    pavadinimas = models.CharField('Pavadinimas', max_length=100)
    aprasymas = models.TextField('Aprašymas', max_length=2000)
    # related_name='irasas_set', irasas_set bus naudojamas iš Artistas objekto, jo įrašams ištraukti
    artistasFK = models.ForeignKey(Artistas, on_delete=models.SET_NULL, null=True, related_name='katalogas_set')
    irasasFK = models.ForeignKey(Irasas, on_delete = models.SET_NULL, null = True, related_name = 'katalog_set')
    def __str__(self):
        return self.pavadinimas