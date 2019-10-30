from django.contrib import admin

# Register your models here.

from .models import User
from Home.models import UserProfile

admin.site.register(UserProfile)