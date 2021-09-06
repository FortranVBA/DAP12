"""Project OC DAP 12 - Account views file."""

from .serializers import StaffSerializer
from .models import Staff, StaffProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

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
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']

    def get_queryset(self):
        queryset = Staff.objects.all()
        profileID = self.request.query_params.get('profile')
        if profileID is not None:
            staff_profile = StaffProfile.objects.get(pk = profileID)
            queryset = queryset.filter(StaffProfileID = staff_profile)
        return queryset

    def get_permissions(self):
        """Instantiate and returns the list of permissions that this view requires."""
        if self.action in ["list", "create", "retrieve", "partial_update", "destroy"]:
            permission_classes = [IsAuthenticated, IsManagement]
        else:
            permission_classes = [NotAllowed]

        return [permission() for permission in permission_classes]