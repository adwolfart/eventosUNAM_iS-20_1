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
    path('<user_mail>/<int:post_id>/', views.EventoUpdate.as_view(), name = 'updateEvento'),
    path('borrarevento/<int:post_id>', views.EventoDelete.as_view(), name = 'deleteEventos'),
    path('listaeventos/', views.EventoList.as_view(), name = 'listaEventos'),

    path('update/evento/<int:post_id>/', views.OnePost.as_view(), name='onePost'),  
    
    path('<int:post_id>/', views.TwoPost.as_view(), name='twoPost'),   
    path('asignar/staff', views.AsignarStaff.as_view(), name='asignarStaff'),  
    path('etiquetas/update', views.Etiquetas.as_view(), name='etiquetas'),   
    path('search/substring', views.Buscar.as_view(), name='registrarU'),
    path('anular/invitacion', views.AnularInvitacion.as_view(), name='anularI'),

    path('mostrar/invitados', views.MostrarInvitados.as_view(), name='mostrarI'),

    path('confirmar/<user_mail>/<int:post_id>', views.ConfirmarAsistencia.as_view(), name='confirmarA'),
    path('confirmar/<correo>/<int:idevento>/<int:id>', views.Confirmacion.as_view(), name = 'confirmacion'),

    path('invitacion/<user_mail>/<int:post_id>', views.Invitaciones.as_view(), name = 'invitacioneS'),
    path('<user_mail>/eventosAsistidos', views.EventosInscritos.as_view(), name = 'vinscritoS'),
    path('<user_mail>/eventosInscritos', views.EventosConfirmados.as_view(), name = 'vconfirmados'),
]

