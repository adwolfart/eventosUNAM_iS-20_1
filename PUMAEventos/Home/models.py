from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django import forms

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    nombre = models.CharField(max_length = 150,default='SOME STRING')
    entidad = models.CharField(max_length = 150, default='SOME STRING')
    avatar = models.ImageField(upload_to='images/',blank=True, null= True)
    
    def __str__(self):  
          return "%s's profile" % self.entidad  

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance) 


class PasswordF(models.Model):
    correo = models.EmailField(max_length = 150, null = False, default = 'null@c.com')
    token = models.CharField(max_length=50, default='null0', null=False)


  