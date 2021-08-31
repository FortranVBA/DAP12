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


