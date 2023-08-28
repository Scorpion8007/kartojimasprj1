from django.db import models

import uuid

class Artistas(models.Model):
    pavadinimas = models.CharField('Pavadinimas', max_length=80)
    metai = models.IntegerField('Pradejo-metai')
    biografija = models.TextField('Bio', max_length = 2000)

    def __str__(self):
        return  self.pavadinimas

class Irasas(models.Model):
    albumas = models.CharField('Albumas', max_length = 100)
    metai_pasirode = models.IntegerField('Pirmo leidimo metai')
    aprasymas = models.TextField('Aprasymas', max_length = 2000)

    artistasFK = models.ForeignKey('Artistas', on_delete=models.SET_NULL, null=True, related_name='irasas_set')

    def __str__(self):
        return self.albumas
