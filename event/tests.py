from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json

class EventTests(APITestCase):
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

    def test_list_event_as_management(self):
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('events-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_event_as_sales(self):
        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('events-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_event_as_support(self):
        url = reverse('login')
        data = {'username': 'StaffSupportA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('events-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_event_with_fake_JWT(self):
        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('events-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_event_without_JWT(self):
        url = reverse('events-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_add_event_as_management(self):
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('events-list')
        data = {
            'ContractID': 1, 
            'Attendees': 800,
            'EventDate': '2001-10-23 13:30:00',
            'Notes': "",
            'SupportContactID': 5,
            'EventStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_event_as_sales(self):
        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('events-list')
        data = {
            'ContractID': 1, 
            'Attendees': 800,
            'EventDate': '2001-10-23 13:30:00',
            'Notes': "",
            'SupportContactID': 5,
            'EventStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_event_as_support(self):
        url = reverse('login')
        data = {'username': 'StaffSupportA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('events-list')
        data = {
            'ContractID': 1, 
            'Attendees': 800,
            'EventDate': '2001-10-23 13:30:00',
            'Notes': "",
            'SupportContactID': 5,
            'EventStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_event_with_fake_JWT(self):
        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('events-list')
        data = {
            'ContractID': 1, 
            'Attendees': 800,
            'EventDate': '2001-10-23 13:30:00',
            'Notes': "",
            'SupportContactID': 5,
            'EventStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_add_event_without_JWT(self):
        url = reverse('events-list')
        data = {
            'ContractID': 1, 
            'Attendees': 800,
            'EventDate': '2001-10-23 13:30:00',
            'Notes': "",
            'SupportContactID': 5,
            'EventStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_modify_event_as_management(self):
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('events-detail', kwargs = {'pk': 1})
        data = {'Attendees': 54321}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Attendees"], 54321)

    def test_modify_event_as_sales_contact(self):
        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('events-detail', kwargs = {'pk': 1})
        data = {'Attendees': 12345}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Attendees"], 12345)

    def test_modify_event_as_sales(self):
        url = reverse('login')
        data = {'username': 'StaffSalesB', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('events-detail', kwargs = {'pk': 1})
        data = {'Attendees': 12345}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_event_as_support_contact(self):
        url = reverse('login')
        data = {'username': 'StaffSupportA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('events-detail', kwargs = {'pk': 1})
        data = {'Attendees': 198273}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Attendees"], 198273)

    def test_modify_event_as_support(self):
        url = reverse('login')
        data = {'username': 'StaffSupportB', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('events-detail', kwargs = {'pk': 1})
        data = {'Attendees': 12345}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_event_with_fake_JWT(self):
        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('events-detail', kwargs = {'pk': 1})
        data = {'Attendees': 12345}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_modify_event_without_JWT(self):
        url = reverse('events-detail', kwargs = {'pk': 1})
        data = {'Attendees': 12345}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
