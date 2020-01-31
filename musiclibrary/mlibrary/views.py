from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from .models import Artist
# from django.views.generic import 
# Create your views here.

# /mlibrary
def index(request):
    artists=Artist.objects.all().order_by('artname')
    context = {
        'Name':'Artist' ,
        'artist': artists,
    }
    return render (request,"mlibrary/index.html",context)


class ListArtist(ListView):
    model = Artist
    template_name='mlibrary/artist-list.html'
    extra_context={
        'title':'Lista Wykonawców',
    }