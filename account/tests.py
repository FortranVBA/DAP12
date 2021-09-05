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
        

    def test_list_user_as_management(self):
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    def test_list_user_as_sales(self):
        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_user_as_support(self):
        url = reverse('login')
        data = {'username': 'StaffSupportA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_user_with_fake_JWT(self):
        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_user_without_JWT(self):
        url = reverse('users-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_add_user_as_management(self):
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-list')
        data = {
            'username': 'NewUser1', 
            'password': 'password',
            'StaffProfileID': '1'
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_user_as_sales(self):
        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-list')
        data = {
            'username': 'NewUser2', 
            'password': 'password',
            'StaffProfileID': '1'
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_user_as_support(self):
        url = reverse('login')
        data = {'username': 'StaffSupportA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-list')
        data = {
            'username': 'NewUser3', 
            'password': 'password',
            'StaffProfileID': '1'
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_user_with_fake_JWT(self):
        token = 'fake_token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-list')
        data = {
            'username': 'NewUser4', 
            'password': 'password',
            'StaffProfileID': '1'
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_add_user_without_JWT(self):
        url = reverse('users-list')
        data = {
            'username': 'NewUser5', 
            'password': 'password',
            'StaffProfileID': '1'
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_modify_user_as_sales(self):
        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-detail', kwargs = {'pk': 2})
        data = {'username': 'ModifUser'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_user_as_support(self):
        url = reverse('login')
        data = {'username': 'StaffSupportA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-detail', kwargs = {'pk': 2})
        data = {'username': 'ModifUser'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_user_with_fake_JWT(self):
        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-detail', kwargs = {'pk': 2})
        data = {'username': 'ModifUser'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_modify_user_without_JWT(self):
        url = reverse('users-detail', kwargs = {'pk': 2})
        data = {'username': 'ModifUser'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_modify_user_as_management(self):
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-detail', kwargs = {'pk': 2})
        data = {'username': 'ModifUser'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "ModifUser")


    def test_delete_user_as_sales(self):

        url = reverse('login')
        data = {'username': 'StaffSalesA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-detail', kwargs = {'pk': 2})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_user_as_support(self):

        url = reverse('login')
        data = {'username': 'StaffSupportA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-detail', kwargs = {'pk': 2})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_user_with_fake_JWT(self):
        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-detail', kwargs = {'pk': 2})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_user_without_JWT(self):
        url = reverse('users-detail', kwargs = {'pk': 2})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_user_as_management(self):
        url = reverse('login')
        data = {'username': 'StaffManagementA', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('users-detail', kwargs = {'pk': 2})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
