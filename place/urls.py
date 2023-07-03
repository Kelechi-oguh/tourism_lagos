from django.urls import path
from .views import Home, PlaceDetailView, New_Place, MainlandListView, IslandListView, BucketListView, Add_to_BucketList



urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('place/<slug:slug>/', PlaceDetailView.as_view(), name='place_detail'),
    path('new_place/', New_Place.as_view(), name='new_place'),
    path('mainland/', MainlandListView.as_view(), name='mainland'),
    path('island/', IslandListView.as_view(), name='island'),
    path('bucket-list/', BucketListView.as_view(), name='bucket-list'),
    path('bucket-list/<slug:slug>/', Add_to_BucketList.as_view(), name='add_to_bucketlist'),
]
