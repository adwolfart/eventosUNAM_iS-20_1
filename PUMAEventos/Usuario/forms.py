from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.forms import ModelForm

from Usuario.models import (Player, Subject, User)

class PlayerSignUpForm(UserCreationForm):
    nUsuario = forms.IntegerField()
    nombre = forms.CharField(label='nombre', max_length=200)
    usuarioTipo = forms.CharField()
    email = forms.EmailField(label='email', max_length=70)
    fechaNacimiento = forms.DateTimeField()
    password = forms.CharField(max_length=200)
    entAcademica = forms.CharField(label='eAcademica', max_length=50)
    # file will be uploaded to MEDIA_ROOT/fotos
    #foto = models.ImageField(label='Image', upload_to='media/fotos/', blank=True)                 

    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_player = True
        user.save()
        player = Player.objects.create(user=user)
        player.interests.add(*self.cleaned_data.get('interests'))
        return user


class PlayerInterestsForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('interests', )
        widgets = {
            'interests': forms.CheckboxSelectMultiple
        }
