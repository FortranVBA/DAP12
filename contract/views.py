"""Project OC DAP 12 - Contract view file."""

from .serializers import ContractSerializer
from .models import Contract
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

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
            return request.user == obj.ClientID.SalesContactID

        return True

class ContractModelViewSet(viewsets.ModelViewSet):
    """Contract viewset."""

    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
    def get_permissions(self):
        """Instantiate and returns the list of permissions that this view requires."""
        if self.action in ["list", 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ["create"]:
            permission_classes = [IsAuthenticated, IsSale]
        elif self.action in ["partial_update"]:
            permission_classes = [IsAuthenticated, IsSalesContactOrManagement]              
        else:
            permission_classes = [NotAllowed]

        return [permission() for permission in permission_classes]
