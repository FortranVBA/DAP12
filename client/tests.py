"""Project OC DAP 12 - Client test file."""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json

from account.models import Staff

class ClientTests(APITestCase):
    """Client test case."""

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
        """Test the client list as a management team member."""

        user = Staff.objects.get(username = 'StaffManagementA')
        self.client.force_authenticate(user)

        url = reverse('clients-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_client_as_management(self):
        """Test the client retrieve as a management team member."""

        user = Staff.objects.get(username = 'StaffManagementA')
        self.client.force_authenticate(user)

        url = reverse('clients-detail', kwargs = {'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["CompanyName"], "ClientA")

    def test_list_client_as_sales(self):
        """Test the client list as a sales team member."""

        user = Staff.objects.get(username = 'StaffSalesA')
        self.client.force_authenticate(user)

        url = reverse('clients-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_client_as_sales(self):
        """Test the client retrieve as a sales team member."""

        user = Staff.objects.get(username = 'StaffSalesA')
        self.client.force_authenticate(user)

        url = reverse('clients-detail', kwargs = {'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["CompanyName"], "ClientA")        

    def test_list_client_as_support(self):
        """Test the client list as a support team member."""

        user = Staff.objects.get(username = 'StaffSupportA')
        self.client.force_authenticate(user)

        url = reverse('clients-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_client_as_support(self):
        """Test the client retrieve as a support team member."""

        user = Staff.objects.get(username = 'StaffSupportA')
        self.client.force_authenticate(user)

        url = reverse('clients-detail', kwargs = {'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["CompanyName"], "ClientA")   

    def test_list_client_with_fake_JWT(self):
        """Test the client list with a fake Json Web Token."""

        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_client_with_fake_JWT(self):
        """Test the client retrieve with a fake Json Web Token."""

        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-detail', kwargs = {'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_client_without_JWT(self):
        """Test the client list without a Json Web Token."""

        url = reverse('clients-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_client_without_JWT(self):
        """Test the client retrieve without a Json Web Token."""

        url = reverse('clients-detail', kwargs = {'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_client_with_contact_filter(self):
        """Test the client list with contact filter."""

        user = Staff.objects.get(username = 'StaffManagementA')
        self.client.force_authenticate(user)

        url = reverse('clients-list')
        response = self.client.get(url, {'contact': 3}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_client_with_status_filter(self):
        """Test the client list with status filter."""

        user = Staff.objects.get(username = 'StaffManagementA')
        self.client.force_authenticate(user)

        url = reverse('clients-list')
        response = self.client.get(url, {'statut': 1}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_client_with_search(self):
        """Test the client list with search filter."""

        user = Staff.objects.get(username = 'StaffManagementA')
        self.client.force_authenticate(user)

        url = reverse('clients-list')
        response = self.client.get(url, {'search': 'entA'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_add_client_as_management(self):
        """Test the client create as a management team member."""

        user = Staff.objects.get(username = 'StaffManagementA')
        self.client.force_authenticate(user)

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
        """Test the client create as a sales team member."""

        user = Staff.objects.get(username = 'StaffSalesA')
        self.client.force_authenticate(user)

        url = reverse('clients-list')
        data = {
            'FirstName': 'JohnD', 
            'LastName': 'SmithD',
            'Email': 'jsd@mail.com',
            'Phone': '+33123456789',
            'Mobile': '+33623456789',
            'CompanyName': 'NewClient2',
            'SalesContactID': 3,
            'ClientStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_client_with_wrong_sales_contact(self):
        """Test the client create with non valid sales contact field."""

        user = Staff.objects.get(username = 'StaffSalesA')
        self.client.force_authenticate(user)

        url = reverse('clients-list')
        data = {
            'FirstName': 'JohnD', 
            'LastName': 'SmithD',
            'Email': 'jsd@mail.com',
            'Phone': '+33123456789',
            'Mobile': '+33623456789',
            'CompanyName': 'NewClient2',
            'SalesContactID': 1,
            'ClientStatutID': 2
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_client_as_support(self):
        """Test the client create as a support team member."""

        user = Staff.objects.get(username = 'StaffSupportA')
        self.client.force_authenticate(user)

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
        """Test the client create as a fake Json Web Token."""

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
        """Test the client create without a Json Web Token."""

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


    def test_modify_client_as_management(self):
        """Test the client update as a management team member."""

        user = Staff.objects.get(username = 'StaffManagementA')
        self.client.force_authenticate(user)

        url = reverse('clients-detail', kwargs = {'pk': 1})
        data = {'CompanyName': 'ModifCompanyName2'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["CompanyName"], "ModifCompanyName2")

    def test_modify_client_as_sales(self):
        """Test the client update as a sales team member who is not the sales contact."""

        user = Staff.objects.get(username = 'StaffSalesB')
        self.client.force_authenticate(user)

        url = reverse('clients-detail', kwargs = {'pk': 1})
        data = {'CompanyName': 'ModifCompanyName'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_client_as_sales_contact(self):
        """Test the client update as the sales contact."""

        user = Staff.objects.get(username = 'StaffSalesA')
        self.client.force_authenticate(user)

        url = reverse('clients-detail', kwargs = {'pk': 1})
        data = {'CompanyName': 'ModifCompanyName'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["CompanyName"], "ModifCompanyName")

    def test_modify_client_with_wrong_sales_contact(self):
        """Test the client update with non valid sales contact field."""

        user = Staff.objects.get(username = 'StaffSalesA')
        self.client.force_authenticate(user)

        url = reverse('clients-detail', kwargs = {'pk': 1})
        data = {'SalesContactID': 1}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_modify_client_as_support(self):
        """Test the client update as a support team member."""

        user = Staff.objects.get(username = 'StaffSupportA')
        self.client.force_authenticate(user)

        url = reverse('clients-detail', kwargs = {'pk': 1})
        data = {'CompanyName': 'ModifCompanyName'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_client_with_fake_JWT(self):
        """Test the client update with a fake Json Web Token."""

        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-detail', kwargs = {'pk': 1})
        data = {'CompanyName': 'ModifCompanyName'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_modify_client_without_JWT(self):
        """Test the client update without Json Web Token."""

        url = reverse('clients-detail', kwargs = {'pk': 1})
        data = {'CompanyName': 'ModifCompanyName'}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_modify_client_status_as_management(self):
        """Test the client status update as a management team member."""

        user = Staff.objects.get(username = 'StaffManagementA')
        self.client.force_authenticate(user)

        user = Staff.objects.get(username = 'StaffManagementA')
        self.client.force_authenticate(user)

        url = reverse('clients-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_client_status_as_sales_contact(self):
        """Test the client status update as the sales contact."""

        user = Staff.objects.get(username = 'StaffSalesA')
        self.client.force_authenticate(user)

        url = reverse('clients-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["ClientStatutID"], 1)

    def test_modify_client_status_as_sales(self):
        """Test the client status update as a sales team member who is not the sales 
        contact."""

        user = Staff.objects.get(username = 'StaffSalesB')
        self.client.force_authenticate(user)

        url = reverse('clients-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_client_status_as_support(self):
        """Test the client status update as a support team member."""

        user = Staff.objects.get(username = 'StaffSupportA')
        self.client.force_authenticate(user)

        url = reverse('clients-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_client_status_with_fake_JWT(self):
        """Test the client status update with a fake Json Web Token."""

        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('clients-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_modify_client_status_without_JWT(self):
        """Test the client status update without a Json Web Token."""

        url = reverse('clients-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_modify_client_status__already_actual(self):
        """Test the client status update of a client that already have this status."""

        user = Staff.objects.get(username = 'StaffSalesA')
        self.client.force_authenticate(user)

        url = reverse('clients-change-status', kwargs = {'pk': 3})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
