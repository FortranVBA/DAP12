from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json

class ContractTests(APITestCase):
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

    def test_list_contract_as_management(self):
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_contract_as_sales(self):
        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_contract_as_support(self):
        url = reverse('login')
        data = {'username': 'StaffSupportA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_contract_with_fake_JWT(self):
        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_contract_without_JWT(self):
        url = reverse('contracts-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_add_contract_as_management(self):
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-list')
        data = {
            'ClientID': 1, 
            'Amount': 888,
            'PaymentDue': '2021-10-22 13:30:00',
            'ContractStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_contract_as_sales(self):
        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-list')
        data = {
            'ClientID': 1, 
            'Amount': 888,
            'PaymentDue': '2021-10-22 13:30:00',
            'ContractStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_contract_as_support(self):
        url = reverse('login')
        data = {'username': 'StaffSupportA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-list')
        data = {
            'ClientID': 1, 
            'Amount': 888,
            'PaymentDue': '2021-10-22 13:30:00',
            'ContractStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_contract_with_fake_JWT(self):
        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-list')
        data = {
            'ClientID': 1, 
            'Amount': 888,
            'PaymentDue': '2021-10-22 13:30:00',
            'ContractStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_add_contract_without_JWT(self):
        url = reverse('contracts-list')
        data = {
            'ClientID': 1, 
            'Amount': 888,
            'PaymentDue': '2021-10-22 13:30:00',
            'ContractStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_modify_contract_as_sales(self):
        url = reverse('login')
        data = {'username': 'StaffSalesB', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-detail', kwargs = {'pk': 1})
        data = {'Amount': 12345}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_contract_as_support(self):
        url = reverse('login')
        data = {'username': 'StaffSupportA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-detail', kwargs = {'pk': 1})
        data = {'Amount': 12345}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_contract_with_fake_JWT(self):
        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-detail', kwargs = {'pk': 1})
        data = {'Amount': 12345}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_modify_contract_without_JWT(self):
        url = reverse('contracts-detail', kwargs = {'pk': 1})
        data = {'Amount': 12345}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_modify_contract_as_management(self):
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-detail', kwargs = {'pk': 1})
        data = {'Amount': 12345}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Amount"], 12345)

    def test_modify_contract_as_sales_contact(self):
        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-detail', kwargs = {'pk': 1})
        data = {'Amount': 54321}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Amount"], 54321)


    def test_list_contract_event_as_management(self):
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-events', kwargs = {'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_contract_event_as_sales(self):
        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-events', kwargs = {'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_contract_event_as_support(self):
        url = reverse('login')
        data = {'username': 'StaffSupportA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-events', kwargs = {'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_contract_event_with_fake_JWT(self):
        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-events', kwargs = {'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_contract_event_without_JWT(self):
        url = reverse('contracts-events', kwargs = {'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_modify_contract_statut_as_management(self):
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_contract_statut_as_sales_contact(self):
        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["ContractStatutID"], 1)

    def test_modify_contract_statut_as_sales(self):
        url = reverse('login')
        data = {'username': 'StaffSalesB', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_contract_statut_as_support(self):
        url = reverse('login')
        data = {'username': 'StaffSupportA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_contract_statut_with_fake_JWT(self):
        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_modify_contract_statut_without_JWT(self):
        url = reverse('contracts-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_modify_contract_statut__already_actual(self):
        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-change-status', kwargs = {'pk': 3})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
