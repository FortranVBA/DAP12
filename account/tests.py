from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

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
            
    def test_succeed_authentification(self):
        """
        Test a successful authentification.
        """
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("refresh", response.data)
