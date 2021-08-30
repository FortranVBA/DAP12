"""Project OC DAP 12 - Account views file."""

from .serializers import RegisterSerializer, StaffSerializer
from .models import Staff
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from rest_framework import viewsets

# Create your views here.
class NotAllowed(permissions.BasePermission):
    """Permission that denies all users."""

    message = "This operation is not allowed."

    def has_permission(self, request, view):
        """Check the object permission."""
        return False

class SignUpView(APIView):
    """Sign up view."""

    permission_classes = [AllowAny]

    def post(self, request):
        """Registration with post request."""
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaffModelsViewSet(viewsets.ModelViewSet):
    """Projects viewset."""

    serializer_class = StaffSerializer
    queryset = Staff.objects.all()

    def get_permissions(self):
        """Instantiate and returns the list of permissions that this view requires."""
        if self.action in ["list", "create", "retrieve"]:
            permission_classes = [AllowAny]
        elif self.action in ["partial_update", "destroy"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [NotAllowed]

        return [permission() for permission in permission_classes]