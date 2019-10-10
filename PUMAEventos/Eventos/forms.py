from django import forms
from django.forms import ModelForm
from .models import Evento,Direccion,Etiquetas


class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'inicio', 'fin', 'n_max', 'descripcion', 'ubicacion']

class DireccionForm(ModelForm):
    class Meta:
        model = Direccion
        fields = ['calle', 'numero', 'cp', 'edo', 'colonia']

class EtiquetasForm(ModelForm):
    class Meta:
        model = Etiquetas
        fields = ['etiqueta']


