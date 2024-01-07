from django.shortcuts import render,redirect 
from album.models import Album
from musician.models import Musicians
from album.forms import AlbumForm
# Create your views here.

def home(request):
    data = Album.objects.all()
    # musician = Musicians.objects.all()
    return render(request, 'home.html',{'data': data}) 


