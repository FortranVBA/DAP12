"""Project OC DAP 12 - Event admin file."""

from django.contrib import admin
from .models import Event, EventStatut

# Register your models here.
admin.site.register(Event)
admin.site.register(EventStatut)