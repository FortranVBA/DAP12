"""Project OC DAP 12 - Event view file."""

from .serializers import EventSerializer
from .models import Event
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class EventModelViewSet(viewsets.ModelViewSet):
    """Event viewset."""

    serializer_class = EventSerializer
    queryset = Event.objects.all()