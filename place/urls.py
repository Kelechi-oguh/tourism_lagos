from django.urls import path
from .views import Home, PlaceDetailView, New_Place, MainlandListView, IslandListView



urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('place/<slug:slug>', PlaceDetailView.as_view(), name='place_detail'),
    path('new_place/', New_Place.as_view(), name='new_place'),
    path('mainland/', MainlandListView.as_view(), name='mainland'),
    path('island/', IslandListView.as_view(), name='island'),
]
