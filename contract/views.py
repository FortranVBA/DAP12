"""Project OC DAP 12 - Contract view file."""

from .serializers import ContractSerializer
from .models import Contract, ContractStatut
from settings.permissions import IsSale, IsStaffContactOrManagement, IsStaffContact
from settings.permissions import AllowedActionsContract
from client.models import Client
from event.serializers import EventSerializer
from event.models import Event
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

# Create your views here.


class ContractModelViewSet(viewsets.ModelViewSet):
    """Contract viewset."""

    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, IsSale, IsStaffContactOrManagement, 
    IsStaffContact, AllowedActionsContract]
 
    def get_queryset(self):
        queryset = Contract.objects.all()
        ClientID = self.request.query_params.get('client')
        if ClientID is not None:
            client = Client.objects.get(pk = ClientID)
            queryset = queryset.filter(ClientID = client)

        StatutID = self.request.query_params.get('statut')
        if StatutID is not None:
            contract_statut = ContractStatut.objects.get(pk = StatutID)
            queryset = queryset.filter(ContractStatutID = contract_statut)

        return queryset

    @action(methods=['get'], detail=True, permission_classes=[IsAuthenticated])
    def events(self, request, pk=None):
        contract = Contract.objects.get(id = pk)
        queryset = Event.objects.filter(ContractID=contract)

        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=True, permission_classes=[IsAuthenticated, 
    IsStaffContact])
    def change_status(self, request, pk=None):
        contract = Contract.objects.get(id = pk)
        self.check_object_permissions(request, contract)
        if contract.ContractStatutID.id != 1: 
            serializer = ContractSerializer(contract, data = {'ContractStatutID': '1'}, 
            partial=True)
        
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        
        return Response({'Error': 'Contract already has this status.'}, 
        status=status.HTTP_400_BAD_REQUEST)
