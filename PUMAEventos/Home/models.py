from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django import forms

class UserProfile(models.Model):
    username = models.CharField(max_length = 150, default = 'User')
    nombre = models.CharField(max_length = 150,default='SOME STRING')
    correo = models.EmailField(max_length = 150, unique= True, default='SOME STRING')
    entidad = models.CharField(max_length = 150, default='SOME STRING')
    password = models.CharField(max_length= 150,default='defaultpass')
    avatar = models.ImageField(upload_to='images/',blank=True)
    
    def __str__(self):  
          return "%s's profile" % self.correo  

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance) 