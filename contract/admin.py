"""Project OC DAP 12 - Contract admin file."""

from django.contrib import admin
from .models import Contract, ContractStatut

# Register your models here.
admin.site.register(Contract)
admin.site.register(ContractStatut)