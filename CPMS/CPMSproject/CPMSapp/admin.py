from .models import MyTicket, Profile
from django.contrib import admin

# from .models import Profile, MyTicket

# Register your models here.
admin.site.register([Profile, MyTicket])