from django.contrib import admin
from musician.models import Musicians
from album.models import Album

admin.site.register(Musicians)
admin.site.register(Album)

# Register your models here.
