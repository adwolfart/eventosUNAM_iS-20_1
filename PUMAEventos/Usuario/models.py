from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_player = models.BooleanField(default=False)


class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)


class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='events')


    def __str__(self):
        return self.name
    

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    events = models.ManyToManyField(Event, through='AttendedEvent')
    interests = models.ManyToManyField(Subject, related_name='interested_players')
    
    def __str__(self):
        return self.user.username

class AttendedEvent(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='attended_events')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attended_events')
    date = models.DateTimeField(auto_now_add=True)




'''

# Create your models here.
from django.urls import reverse
from DjangoBlog.utils import get_current_site
from django.utils.timezone import now

# Create your models here.

class Usuario(models.Model):
    nUsuario = models.IntegerField()
    nombre = models.CharField(label='nombre', max_length=200, null=False)
    usuarioTipo = models.CharField()
    email = models.EmailField(label='email', max_length=70)
    fechaNacimiento = models.DateTimeField()
    password = models.charField(max_length=200, null=False)
    entAcademica = models.CharField(label='eAcademica', max_length=50, null=False)
    # file will be uploaded to MEDIA_ROOT/fotos
    foto = models.ImageField(label='Image', upload_to='media/fotos/', blank=True)                 


    class Meta:
        db_table = 'usuario'
'''
