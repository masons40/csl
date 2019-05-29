from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('about/', views.About, name='about'),
	path('InformationforParticipants/', views.InformationforParticipants, name='InformationforParticipants'),
	path('InformationforResearchers/', views.InformationforResearchers, name='InformationforResearchers'),
	path('NewsAndPublications/', views.NewsAndPublications, name='NewsAndPublications'),
	path('PV/', views.PV, name='PV'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)