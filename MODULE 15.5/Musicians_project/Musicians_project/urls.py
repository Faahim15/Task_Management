
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [ 
    path('',views.home, name='homepage'),
    path('admin/', admin.site.urls),
    path('album/', include('album.urls')),
    path('musician/', include('musician.urls')), 
    
]
