from django import forms
from django.forms import ModelForm
from .models import Evento,Direccion,Etiquetas


class EventoForm(forms.ModelForm):
    fecha_de_inicio = forms.DateField(widget=forms.DateInput(attrs={'placeholder': "mm/dd/yyyy"}))
    fecha_final = forms.DateField(widget=forms.DateInput(attrs={'placeholder': "mm/dd/yyyy"}))
    
    class Meta:
        model = Evento
        fields = [
            'titulo', 
            'fecha_de_inicio', 
            'hora_de_inicio',
            'fecha_final',
            'hora_final', 
            'cupo_maximo', 
            'descripcion', 
            'ubicacion',
        ]


        
class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion

        fields = [
            'calle', 
            'numero', 
            'cp', 
            'edo', 
            'colonia',
            ]

        labels = {
            'cp': 'Codigo Postal',
            'edo': 'Estado',
        }

class EtiquetasForm(forms.ModelForm):


    lista = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "etiqueta1, etiqueta2, etc..."}))

    class Meta:

        model = Etiquetas 

        fields = ['lista']
        
        labels = {
            'lista': 'Etiquetas del evento: ',
        }


