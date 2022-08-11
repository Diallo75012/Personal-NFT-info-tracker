from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [
    path('nfts', views.nfts, name="nfts"),
    path('<int:pk>/nfts-update', views.nfts_update, name="nfts_update"),
    path('<int:pk>/nfts-delete', views.nfts_delete, name="nfts_delete"),
]