"""Project OC DAP 10 - Comments view file."""

from .serializers import ClientSerializer
from .models import Client, ClientStatut
from settings.permissions import IsSale, IsStaffContactOrManagement, IsStaffContact
from settings.permissions import AllowedActionsClient
from account.models import Staff
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import filters

# Create your views here.

class ClientModelViewSet(viewsets.ModelViewSet):
    """Client viewset."""

    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['CompanyName']
    permission_classes = [IsAuthenticated, IsSale, IsStaffContactOrManagement, 
    IsStaffContact, AllowedActionsClient]

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

    @action(methods=['post'], detail=True, permission_classes=[IsAuthenticated, 
    IsStaffContact])
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
