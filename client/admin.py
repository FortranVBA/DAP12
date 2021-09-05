from django.contrib import admin
from .models import Client, ClientStatut

# Register your models here.
admin.site.register(Client)
admin.site.register(ClientStatut)