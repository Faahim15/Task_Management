from django.shortcuts import render,redirect
from TaskCategory.forms import TaskCategoryForm

# Create your views here.

def AddCategory(request):
    
    task_categoryForm = TaskCategoryForm()
    if request.method == 'POST':
        task_categoryForm = TaskCategoryForm(request.POST) 
        if task_categoryForm.is_valid():
            task_categoryForm.save() 
            return redirect('homepage')
    
    return render(request, 'add_task.html',{'form':task_categoryForm})
    