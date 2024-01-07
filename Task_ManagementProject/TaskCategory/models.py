from django.db import models
from TaskModel.models import TaskModel
# Create your models here.
class TaskCategory(models.Model):
    category_name = models.CharField(max_length=50)
    task_model = models.ManyToManyField(TaskModel, blank=True) 

    def __str__(self) -> str:
        return self.category_name
 