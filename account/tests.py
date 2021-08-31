from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

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
        self.assertIn("access", response.data)

    def test_failed_authentification(self):
        url = reverse('login')
        data = {'username': 'UnknownUser', 'password': 'password'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("No active account found with the given credentials", 
        response.data['detail'])

    def test_add_user_as_management(self):
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-list')
        data = {
            'username': 'NewUser', 
            'password': 'password',
            'StaffProfileID': '1'
            }
        response = self.client.post(url, data, format='json')

        print(response)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_user_as_sales(self):
        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-list')
        data = {
            'username': 'NewUser', 
            'password': 'password',
            'StaffProfileID': '1'
            }
        response = self.client.post(url, data, format='json')

        print(response)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

