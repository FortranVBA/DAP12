"""Project OC DAP 10 - Comments view file."""

from .serializers import ClientSerializer
from .models import Client
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ClientModelViewSet(viewsets.ModelViewSet):
    """Client viewset."""

    serializer_class = ClientSerializer
    queryset = Client.objects.all()