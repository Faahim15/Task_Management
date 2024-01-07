from django.shortcuts import render,redirect 
from . import forms 
from album.models import Album
from album.forms import AlbumForm
from musician.models import Musicians

# Create your views here.

def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save() 
            return redirect('add_album') 
    else:
        album_form = forms.AlbumForm() 
    return render(request,'add_album.html',{'form':album_form})

def edit_album(request,id):
    album = Album.objects.get(pk =id)
    data = AlbumForm(instance = album)

    if request.method == 'POST':
        date = AlbumForm(request.POST,instance=album) 
        if date.is_valid():
            date.save() 
            return redirect('homepage')
    return render(request,'add_album.html',{'form': data}) 

def delete_musician(request,id):
    musician = Musicians.objects.get(pk=id)
    musician.delete()
    return redirect('homepage')