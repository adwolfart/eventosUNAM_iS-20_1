from django.contrib import admin

# Register your models here.
from Eventos.models import Etiquetas, Direccion, Evento

admin.site.register(Etiquetas)
admin.site.register(Direccion)
admin.site.register(Evento)
