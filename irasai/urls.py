from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage-url'),
    path('artistai/', views.artistai, name='artistai-visi-url'),
    path('artistai/<int:artistas_id>', views.artistas, name='artistas-vienas-url'),
    path('irasai', views.IrasasListView.as_view(), name='irasai-visi-url'),
    path('irasai/<int:pk>', views.IrasasDetailView.as_view(), name='irasas-vienas-url'),
    path('katalogai', views.KatalogasListView.as_view(), name = 'katalogai-visi-url'),
    path('katalogai/<int:pk>', views.KatalogasDetailView.as_view(), name = 'katalogas-vienas-url'),
    path('paieska/', views.search, name = 'paieska-url'),
    path('paiesk/', views.searc, name = 'paiesk-url'),
]