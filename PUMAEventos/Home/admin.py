from django.contrib import admin

# Register your models here.

from .models import User
from Home.models import UserProfile, PasswordF

admin.site.register(UserProfile)
admin.site.register(PasswordF)