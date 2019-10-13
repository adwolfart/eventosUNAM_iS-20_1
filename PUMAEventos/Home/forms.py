from django import forms
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password')


class OrgForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    correo = forms.EmailField(max_length=100)
    usuario = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)