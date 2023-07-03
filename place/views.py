from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View, generic
from .forms import PlaceForm
from .models import Place, BucketList


# Create your views here.
class Home(generic.TemplateView):
    template_name = 'home.html'


class New_Place(View):
    def post(self, request):
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            context = {"form": form}
        return render(request, 'new_place.html', context=context)

    def get(self, request):
        form = PlaceForm()
        context = {"form": form}
        return render(request, 'new_place.html', context=context)
    

class PlaceDetailView(generic.DetailView):
    model = Place
    context_object_name = 'place'
    template_name = 'place_detail.html'


class MainlandListView(generic.ListView):
    model = Place
    queryset = Place.objects.filter(location='mainland')
    template_name = 'location.html'


class IslandListView(generic.ListView):
    model = Place
    queryset = Place.objects.filter(location='island')
    template_name = 'location.html'


class Add_to_BucketList(View):
    def post(self, request, slug):
        if request.user.is_authenticated:
            bucket_list = BucketList.objects.get(user=request.user)
            place_obj = Place.objects.get(slug=slug)

            if place_obj:
                bucket_list.places.add(place_obj)
                bucket_list.save()
                messages.success(request, f"*{place_obj.name}* Added to Bucket List")

        return redirect(self.request.META.get('HTTP_REFERER'))



class BucketListView(View):
    def get(self, request, *args, **kwargs):
        context = {"object_list": None}

        if request.user.is_authenticated:
            bucket_exists = BucketList.objects.filter(user=request.user)
            if not bucket_exists:
                bucket_list = BucketList(user=request.user)
                bucket_list.save()

            bucket_list = BucketList.objects.get(user=request.user)
            if bucket_list:
                context = {"object_list": bucket_list.places.all()}
            
        return render(request, 'bucket_list.html', context=context)
