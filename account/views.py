"""Project OC DAP 12 - Account views file."""

from .serializers import StaffSerializer
from .models import Staff, StaffProfile
from settings.permissions import AllowedActionsAccount, IsManagement
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

# Create your views here.

class StaffModelsViewSet(viewsets.ModelViewSet):
    """Projects viewset."""

    serializer_class = StaffSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    permission_classes = [IsAuthenticated, IsManagement, AllowedActionsAccount]

    def get_queryset(self):
        queryset = Staff.objects.all()
        profileID = self.request.query_params.get('profile')
        if profileID is not None:
            staff_profile = StaffProfile.objects.get(pk = profileID)
            queryset = queryset.filter(StaffProfileID = staff_profile)
        return queryset
