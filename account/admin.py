"""Project OC DAP 12 - Account admin file."""

from django.contrib import admin
from .models import Staff, StaffProfile

# Register your models here.
admin.site.register(Staff)
admin.site.register(StaffProfile)

