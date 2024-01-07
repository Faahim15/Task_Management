
from django.urls import path
from album.views import add_album,edit_album,delete_musician
urlpatterns = [
    path('add/',add_album, name='add_album'),
    path('edit/<int:id>', edit_album, name='edit_album'),
    path('delete/<int:id>', delete_musician, name='delete_musician'),
]