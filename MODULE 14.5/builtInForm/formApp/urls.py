from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from formApp.views import createForms, createModel,ModelOneView

urlpatterns = [
    path('', createForms, name='home'), 
    path('model/', createModel, name='model'),
    path('modelOne/', ModelOneView, name='modelOne'),
]

# Add the following lines to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
