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
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)


    def test_retrieve_client_as_management(self):
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-detail', kwargs = {'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["CompanyName"], "ClientA")

    def test_list_client_as_sales(self):
        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_client_as_support(self):
        url = reverse('login')
        data = {'username': 'StaffSupportA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_client_with_fake_JWT(self):
        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_client_without_JWT(self):

        url = reverse('clients-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_add_client_as_management(self):
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-list')
        data = {
            'FirstName': 'JohnD', 
            'LastName': 'SmithD',
            'Email': 'jsd@mail.com',
            'Phone': '+33123456789',
            'Mobile': '+33623456789',
            'CompanyName': 'NewClient1',
            'SalesContactID': 2,
            'ClientStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_client_as_sales(self):
        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-list')
        data = {
            'FirstName': 'JohnD', 
            'LastName': 'SmithD',
            'Email': 'jsd@mail.com',
            'Phone': '+33123456789',
            'Mobile': '+33623456789',
            'CompanyName': 'NewClient2',
            'SalesContactID': 2,
            'ClientStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_add_client_as_support(self):
        url = reverse('login')
        data = {'username': 'StaffSupportA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-list')
        data = {
            'FirstName': 'JohnD', 
            'LastName': 'SmithD',
            'Email': 'jsd@mail.com',
            'Phone': '+33123456789',
            'Mobile': '+33623456789',
            'CompanyName': 'NewClient3',
            'SalesContactID': 2,
            'ClientStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_client_with_fake_JWT(self):
        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-list')
        data = {
            'FirstName': 'JohnD', 
            'LastName': 'SmithD',
            'Email': 'jsd@mail.com',
            'Phone': '+33123456789',
            'Mobile': '+33623456789',
            'CompanyName': 'NewClient4',
            'SalesContactID': 2,
            'ClientStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_add_client_without_JWT(self):
        url = reverse('clients-list')
        data = {
            'FirstName': 'JohnD', 
            'LastName': 'SmithD',
            'Email': 'jsd@mail.com',
            'Phone': '+33123456789',
            'Mobile': '+33623456789',
            'CompanyName': 'NewClient5',
            'SalesContactID': 2,
            'ClientStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_modify_client_as_sales(self):
        url = reverse('login')
        data = {'username': 'StaffSalesB', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-detail', kwargs = {'pk': 1})
        data = {'CompanyName': 'ModifCompanyName'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_client_as_support(self):
        url = reverse('login')
        data = {'username': 'StaffSupportA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-detail', kwargs = {'pk': 1})
        data = {'CompanyName': 'ModifCompanyName'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_client_with_fake_JWT(self):
        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-detail', kwargs = {'pk': 1})
        data = {'CompanyName': 'ModifCompanyName'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_modify_client_without_JWT(self):
        url = reverse('clients-detail', kwargs = {'pk': 1})
        data = {'CompanyName': 'ModifCompanyName'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_modify_client_as_sales_contact(self):
        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-detail', kwargs = {'pk': 1})
        data = {'CompanyName': 'ModifCompanyName'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["CompanyName"], "ModifCompanyName")

    def test_modify_client_as_management(self):
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-detail', kwargs = {'pk': 1})
        data = {'CompanyName': 'ModifCompanyName2'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["CompanyName"], "ModifCompanyName2")
