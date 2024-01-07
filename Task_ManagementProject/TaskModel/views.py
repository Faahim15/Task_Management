from django.shortcuts import render,redirect
from TaskModel.forms import TaskModelForm 
from . models import TaskModel
# Create your views here.

def add_task(request):
    add_taskModel = TaskModelForm()
    if request.method == 'POST':
        add_taskModel = TaskModelForm(request.POST)
        if add_taskModel.is_valid():
            add_taskModel.save()
            return redirect('homepage')
    return render(request, 'add_task_model.html',{'form': add_taskModel }) 

def edit_task(request,id):
    post = TaskModel.objects.get(pk = id) 
    post_form = TaskModelForm(instance=post) 

    if request.method == 'POST':
        task = TaskModelForm(request.POST, instance=post)
        if task.is_valid():
            task.save()
            return redirect('homepage') 
        
    return render(request, 'add_task_model.html',{'form': post_form}) 


def delete_task(request, id):
    card = TaskModel.objects.get(pk = id)
    card.delete()
    return redirect('homepage')
