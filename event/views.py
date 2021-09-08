"""Project OC DAP 12 - Event view file."""

from .serializers import EventSerializer
from .models import Event, EventStatut
from settings.permissions import IsSale, IsStaffContactOrManagement
from settings.permissions import AllowedActionsEvent
from account.models import Staff
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

# Create your views here.

class EventModelViewSet(viewsets.ModelViewSet):
    """Event viewset."""

    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsSale, IsStaffContactOrManagement, 
    AllowedActionsEvent]

    def get_queryset(self):
        queryset = Event.objects.all()
        StaffContactID = self.request.query_params.get('contact')
        if StaffContactID is not None:
            staff_contact = Staff.objects.get(pk = StaffContactID)
            queryset = queryset.filter(SupportContactID = staff_contact)

        StatutID = self.request.query_params.get('statut')
        if StatutID is not None:
            contract_statut = EventStatut.objects.get(pk = StatutID)
            queryset = queryset.filter(EventStatutID = contract_statut)

        return queryset

    def list(self, request, *args, **kwargs):
        """List all events."""
        past_events = Event.objects.filter(EventDate__lt = datetime.now())

        for event in past_events:
            serializer = EventSerializer(event, data = {'EventStatutID': 1}, 
            partial=True)
            if serializer.is_valid():
                serializer.save()

        scheduled_events = Event.objects.filter(EventDate__gte = datetime.now())

        for event in scheduled_events:
            serializer = EventSerializer(event, data = {'EventStatutID': 2}, 
            partial=True)
            if serializer.is_valid():
                serializer.save()

        return super().list(request, args, kwargs)
        