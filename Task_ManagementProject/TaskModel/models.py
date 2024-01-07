from django.db import models

# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length=50)
    task_description = models.TextField()  # Change from CharField to TextField
    is_completed = models.BooleanField(default=False)
    Task_assign_date = models.DateField()

    def __str__(self) -> str:
        return self.task_title
