"""Project OC DAP 12 - Event view file."""

from .serializers import EventSerializer
from .models import Event, EventStatut
from account.models import Staff
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

# Create your views here.
class NotAllowed(permissions.BasePermission):
    """Permission that denies all users."""

    message = "This operation is not allowed."

    def has_permission(self, request, view):
        """Check the object permission."""
        return False

class IsSale(permissions.BasePermission):
    """Permission that denies all users."""

    message = "You must be part of sales team for this operation."

    def has_permission(self, request, view):
        """Check the object permission."""
        return request.user.StaffProfileID.Name == "Vente"

class IsStaffContactOrManagement(permissions.BasePermission):
    """Permission checking if user is a project contributor or author."""

    message = "You must be the sales contact of this project or from management team."

    def has_permission(self, request, view):
        """Check the object permission."""
        profile_name = request.user.StaffProfileID.Name
        return profile_name in ["Vente", "Gestion", "Support"]

    def has_object_permission(self, request, view, obj):
        """Check the object permission."""
        if request.user.StaffProfileID.Name == "Vente":
            return request.user == obj.ContractID.ClientID.SalesContactID

        if request.user.StaffProfileID.Name == "Support":
            return request.user == obj.SupportContactID

        return True

class EventModelViewSet(viewsets.ModelViewSet):
    """Event viewset."""

    serializer_class = EventSerializer

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

    def get_permissions(self):
        """Instantiate and returns the list of permissions that this view requires."""
        if self.action in ["list", 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ["create"]:
            permission_classes = [IsAuthenticated, IsSale]
        elif self.action in ["partial_update"]:
            permission_classes = [IsAuthenticated, IsStaffContactOrManagement]              
        else:
            permission_classes = [NotAllowed]

        return [permission() for permission in permission_classes]

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
        