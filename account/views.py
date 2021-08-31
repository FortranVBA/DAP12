"""Project OC DAP 12 - Account views file."""

from .serializers import StaffSerializer
from .models import Staff
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class NotAllowed(permissions.BasePermission):
    """Permission that denies all users."""

    message = "This operation is not allowed."

    def has_permission(self, request, view):
        """Check the object permission."""
        return False

class IsManagement(permissions.BasePermission):
    """Permission that denies all users."""

    message = "You must be part of management team for this operation."

    def has_permission(self, request, view):
        """Check the object permission."""
        return request.user.StaffProfileID.Name == "Gestion"

class StaffModelsViewSet(viewsets.ModelViewSet):
    """Projects viewset."""

    serializer_class = StaffSerializer
    queryset = Staff.objects.all()

    def get_permissions(self):
        """Instantiate and returns the list of permissions that this view requires."""
        if self.action in ["list", "create", "retrieve", "partial_update", "destroy"]:
            permission_classes = [IsAuthenticated, IsManagement]
        else:
            permission_classes = [NotAllowed]

        return [permission() for permission in permission_classes]