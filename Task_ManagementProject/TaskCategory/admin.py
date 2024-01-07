from django.contrib import admin
from TaskCategory.models import TaskCategory
from TaskModel.models import TaskModel
# Register your models here.
admin.site.register(TaskCategory)
admin.site.register(TaskModel)
