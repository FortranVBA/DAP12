from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json

class ClientTests(APITestCase):
    fixtures = [
        "staffprofile_data.json", 
        "clientstatut_data.json", 
        "contractstatut_data.json", 
        "eventstatut_data.json", 
        "staff_data.json", 
        "client_data.json", 
        "contract_data.json", 
        "event_data.json",
        ]   

    def test_list_client_as_management(self):
        """
        Test a successful authentification.
        """
        url = reverse('clients-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_client_as_management(self):
        """
        Test a successful authentification.
        """
        url = reverse('clients-detail', kwargs = {'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["CompanyName"], "ClientA")


#def test_list_client_as_management(client):
#    response = client.post('/login/', data={"UserName":"StaffGestionA"})
#    JWT = response.JWT

#    response = client.get('/clients/')
#    assert response.status_code == 200
#    assert b"ClientA" in response.data
#    assert b"ClientB" in response.data
#    assert b"ClientC" in response.data