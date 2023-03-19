from django.urls import path
from .views import index, detail, acceuil,contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('produit', index, name='Produit'),
    path('<int:myid>', detail, name='detail'),
    path('', acceuil, name='Home'),
    path('contact', contact, name='Contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)