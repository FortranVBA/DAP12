"""Project OC DAP 10 - Comments view file."""

from .serializers import ClientSerializer
from .models import Client, ClientStatut
from account.models import Staff
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

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

class IsSaleContact(permissions.BasePermission):
    """Permission that denies all users."""

    message = "You must be the sales contact for this operation."

    def has_permission(self, request, view):
        """Check the object permission."""
        return request.user.StaffProfileID.Name == "Vente"

    def has_object_permission(self, request, view, obj):
        """Check the object permission."""
        return request.user == obj.SalesContactID

class IsSalesContactOrManagement(permissions.BasePermission):
    """Permission checking if user is a project contributor or author."""

    message = "You must be the sales contact of this project or from management team."

    def has_permission(self, request, view):
        """Check the object permission."""
        profile_name = request.user.StaffProfileID.Name
        return (profile_name == "Vente") or (profile_name == "Gestion")

    def has_object_permission(self, request, view, obj):
        """Check the object permission."""
        if request.user.StaffProfileID.Name == "Vente":
            return request.user == obj.SalesContactID

        return True

class ClientModelViewSet(viewsets.ModelViewSet):
    """Client viewset."""

    serializer_class = ClientSerializer

    def get_queryset(self):
        queryset = Client.objects.all()
        SalesContactID = self.request.query_params.get('contact')
        if SalesContactID is not None:
            sales_contact = Staff.objects.get(pk = SalesContactID)
            queryset = queryset.filter(SalesContactID = sales_contact)

        StatutID = self.request.query_params.get('statut')
        if StatutID is not None:
            client_statut = ClientStatut.objects.get(pk = StatutID)
            queryset = queryset.filter(ClientStatutID = client_statut)

        return queryset

    def get_permissions(self):
        """Instantiate and returns the list of permissions that this view requires."""
        if self.action in ["list", 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ["create"]:
            permission_classes = [IsAuthenticated, IsSale]
        elif self.action in ["partial_update"]:
            permission_classes = [IsAuthenticated, IsSalesContactOrManagement]
        elif self.action in ["change_status"]:
            permission_classes = [IsAuthenticated, IsSaleContact]
        else:
            permission_classes = [NotAllowed]

        return [permission() for permission in permission_classes]

    @action(methods=['post'], detail=True, permission_classes=[IsAuthenticated, 
    IsSaleContact])
    def change_status(self, request, pk=None):
        client = Client.objects.get(id = pk)
        self.check_object_permissions(request, client)
        if client.ClientStatutID.id != 1: 
            serializer = ClientSerializer(client, data = {'ClientStatutID': '1'}, 
            partial=True)
        
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        
        return Response({'Error': 'Client already has this status.'}, 
        status=status.HTTP_400_BAD_REQUEST)
