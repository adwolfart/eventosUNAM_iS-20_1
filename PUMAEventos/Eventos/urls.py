from django.urls import path
from django.urls import include, path
from . import views

app_name = 'Eventos'
urlpatterns = [
    # Funtion view
    # path('', views.index, name='index'),
    # Class-based Views
    #path('', views.Index.as_view(), name='index'),
    

    path('crearevento/', views.EventoCreate.as_view(), name = 'crearEvento'),
    path('updateevento/', views.EventoUpdate.as_view(), name = 'updateEvento'),
    path('borrarevento/', views.EventoDelete.as_view(), name = 'deleteEventos'),
    path('listaeventos/', views.EventoList.as_view(), name = 'listaEventos'),

    path('<int:post_id>/', views.OnePost.as_view(), name='onePost'),    
    
]

