from django import forms
from django.forms import ModelForm
from django.core.files.images import get_image_dimensions

from Home.models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password')


class OrgForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    correo = forms.EmailField(max_length=100)

class DelForm(forms.Form):
    correo = forms.EmailField(max_length=100)


class Userform(forms.Form):
    username = forms.CharField(label = 'nombre', max_length = 100)
    password = forms.CharField(label = 'password')

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ('nombre', 'entidad', 'avatar')

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        return avatar

class PasswordResetF(forms.Form):
    password = forms.CharField(max_length=50)
  