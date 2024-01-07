from TaskModel.models import TaskModel
from django import forms

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        widgets = {
            'Task_assign_date': forms.DateInput(attrs={'type': 'date'}),
        }
        