from django.shortcuts import render
from formApp.forms import CreateBuilInForm
from formApp.models import Dbproject,ModelOne

# Create your views here.

def createForms (request):
    form = CreateBuilInForm(request.POST,request.FILES) 
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,'home.html',{'form':form})

def createModel(request):
    data = Dbproject.objects.all()

    return render(request, 'model.html',{'data': data})
def ModelOneView(request):

    data = ModelOne.objects.all()

    return render(request, 'modelone.html',{'data': data})


