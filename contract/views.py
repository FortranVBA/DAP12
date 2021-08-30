"""Project OC DAP 12 - Contract view file."""

from .serializers import ContractSerializer
from .models import Contract
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ContractModelViewSet(viewsets.ModelViewSet):
    """Contract viewset."""

    serializer_class = ContractSerializer
    queryset = Contract.objects.all()