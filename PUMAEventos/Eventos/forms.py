from django import forms
from django.forms import ModelForm
from .models import Evento

class EventoForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    fecha_de_inicio = forms.DateField()
    #hora_de_inicio = forms.TimeField()
    #fecha_final = forms.DateField()
    #hora_final = forms.TimeField()
    cupo_maximo = forms.IntegerField()
    descripcion = forms.CharField()
    direccion = forms.CharField(max_length=100)
    ubicacion = forms.CharField(max_length=100)
    #entidad = forms.CharField(max_length = 150)
    correo = forms.EmailField(max_length = 150)


class DelEventoForm(forms.Form):
    correo = forms.EmailField()
    id = forms.IntegerField()


class UpdateForm(forms.Form):
    """    
        titulo = forms.CharField(max_length=100)
        fecha_de_inicio = forms.DateField()
        hora_de_inicio = forms.TimeField()
        fecha_final = forms.DateField()
        hora_final = forms.TimeField()
        cupo_maximo = forms.IntegerField()
        descripcion = forms.CharField()
        ubicacion = forms.CharField(max_length=100)
        entidad = forms.CharField(max_length = 150)  
        correo = forms.EmailField(max_length = 150)
        id = forms.IntegerField() 
    """

    titulo = forms.CharField(max_length=100)
    fecha_de_inicio = forms.DateField()
    #hora_de_inicio = forms.TimeField()
    #fecha_final = forms.DateField()
    #hora_final = forms.TimeField()
    cupo_maximo = forms.IntegerField()
    descripcion = forms.CharField()
    direccion = forms.CharField(max_length=100)
    ubicacion = forms.CharField(max_length=100)
    #entidad = forms.CharField(max_length = 150)
    correo = forms.EmailField(max_length = 150)    