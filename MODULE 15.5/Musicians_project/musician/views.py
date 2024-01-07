from django.shortcuts import render,redirect 
from musician.forms import MusicianForm
from musician.models import Musicians

# Create your views here.

def add_musician(request):
    if request.method == 'POST':
        musician_form = MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save() 
            return redirect('add_musician') 
    else:
        musician_form = MusicianForm() 
    return render(request,'add_musician.html',{'form':musician_form}) 

def edit_musician(request,id):
    album = Musicians.objects.get(pk =id)
    data = MusicianForm(instance = album)

    if request.method == 'POST':
        date = MusicianForm(request.POST,instance=album) 
        if date.is_valid():
            date.save() 
            return redirect('homepage')
    return render(request,'add_musician.html',{'form': data}) 