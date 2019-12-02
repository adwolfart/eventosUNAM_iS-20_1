from django.contrib import admin

# Register your models here.
from Eventos.models import Evento,RegEvento,AsigStaff

admin.site.register(Evento)
admin.site.register(RegEvento)
admin.site.register(AsigStaff)