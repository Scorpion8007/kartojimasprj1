from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='namu_puslapis_url'),
               path('artistai/', views.artistai, name='artistai-visi-url')

]