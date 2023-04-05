from django.shortcuts import render
from django.views import View, generic
from .forms import PlaceForm
from .models import Place

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