from django.shortcuts import render,redirect 
from TaskCategory.models import TaskCategory

def home(request):
    data = TaskCategory.objects.all()
   
    return render(request, 'home.html',{'data': data}) 

