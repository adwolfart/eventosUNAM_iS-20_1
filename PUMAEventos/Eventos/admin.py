from django.contrib import admin

# Register your models here.
from Eventos.models import Evento,RegEvento

admin.site.register(Evento)
admin.site.register(RegEvento)