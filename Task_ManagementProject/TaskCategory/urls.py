from django.urls import path
from TaskCategory.views import AddCategory
urlpatterns = [
  path('add/', AddCategory, name='add_category'),
]