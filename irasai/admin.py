from django.contrib import admin
from .models import Artistas, Irasas, Katalogas

# Register your models here.

admin.site.register(Artistas)
admin.site.register(Irasas)
admin.site.register(Katalogas)