
from django.urls import path
from musician.views import add_musician,edit_musician
urlpatterns = [
    path('add/',add_musician, name='add_musician'),
    path('edit/<int:id>', edit_musician, name='edit_musician'),
]