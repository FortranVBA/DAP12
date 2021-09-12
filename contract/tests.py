"""Project OC DAP 12 - Contract test file."""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json

from account.models import Staff

class ContractTests(APITestCase):
    """Contract test case."""

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
        """Test the contract list as a management team member."""

        user = Staff.objects.get(username = 'StaffManagementA')
        self.client.force_authenticate(user)

        url = reverse('contracts-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_contract_as_sales(self):
        """Test the contract list as a sales team member."""

        user = Staff.objects.get(username = 'StaffSalesA')
        self.client.force_authenticate(user)

        url = reverse('contracts-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_contract_as_support(self):
        """Test the contract list as a support team member."""

        user = Staff.objects.get(username = 'StaffSupportA')
        self.client.force_authenticate(user)

        url = reverse('contracts-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_contract_with_fake_JWT(self):
        """Test the contract list with a fake Json Web Token."""

        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_contract_without_JWT(self):
        """Test the contract list without a Json Web Token."""

        url = reverse('contracts-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_contract_with_client_filter(self):
        """Test the contract list with client filter."""

        user = Staff.objects.get(username = 'StaffManagementA')
        self.client.force_authenticate(user)

        url = reverse('contracts-list')
        response = self.client.get(url, {'client': 3}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_contract_with_status_filter(self):
        """Test the contract list with status filter."""

        user = Staff.objects.get(username = 'StaffManagementA')
        self.client.force_authenticate(user)

        url = reverse('contracts-list')
        response = self.client.get(url, {'statut': 2}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    def test_add_contract_as_management(self):
        """Test the contract create as a management team member."""

        user = Staff.objects.get(username = 'StaffManagementA')
        self.client.force_authenticate(user)

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
        """Test the contract create as a sales team member."""

        user = Staff.objects.get(username = 'StaffSalesA')
        self.client.force_authenticate(user)

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
        """Test the contract create as a support team member."""

        user = Staff.objects.get(username = 'StaffSupportA')
        self.client.force_authenticate(user)

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
        """Test the contract create with a fake Json Web Token."""

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
        """Test the contract create without a Json Web Token."""

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
        """Test the contract update as a sales team member who is not the sales contact."""

        user = Staff.objects.get(username = 'StaffSalesB')
        self.client.force_authenticate(user)

        url = reverse('contracts-detail', kwargs = {'pk': 1})
        data = {'Amount': 12345}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_contract_as_support(self):
        """Test the contract update as a support team member."""

        user = Staff.objects.get(username = 'StaffSupportA')
        self.client.force_authenticate(user)        

        url = reverse('contracts-detail', kwargs = {'pk': 1})
        data = {'Amount': 12345}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_contract_with_fake_JWT(self):
        """Test the contract update with a fake Json Web Token."""

        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-detail', kwargs = {'pk': 1})
        data = {'Amount': 12345}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_modify_contract_without_JWT(self):
        """Test the contract update without a Json Web Token."""

        url = reverse('contracts-detail', kwargs = {'pk': 1})
        data = {'Amount': 12345}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_modify_contract_as_management(self):
        """Test the contract update as a management team member."""

        user = Staff.objects.get(username = 'StaffManagementA')
        self.client.force_authenticate(user)       

        url = reverse('contracts-detail', kwargs = {'pk': 1})
        data = {'Amount': 12345}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Amount"], 12345)

    def test_modify_contract_as_sales_contact(self):
        """Test the contract update as the sales contact."""

        user = Staff.objects.get(username = 'StaffSalesA')
        self.client.force_authenticate(user)    

        url = reverse('contracts-detail', kwargs = {'pk': 1})
        data = {'Amount': 54321}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Amount"], 54321)


    def test_list_contract_event_as_management(self):
        """Test the event listing by contract as a management team member."""

        user = Staff.objects.get(username = 'StaffManagementA')
        self.client.force_authenticate(user)  

        url = reverse('contracts-events', kwargs = {'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_contract_event_as_sales(self):
        """Test the event listing by contract as a sales team member."""

        user = Staff.objects.get(username = 'StaffSalesA')
        self.client.force_authenticate(user)  

        url = reverse('contracts-events', kwargs = {'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_contract_event_as_support(self):
        """Test the event listing by contract as a support team member."""

        user = Staff.objects.get(username = 'StaffSupportA')
        self.client.force_authenticate(user)  

        url = reverse('contracts-events', kwargs={'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_contract_event_with_fake_JWT(self):
        """Test the event listing by contract with a fake Json Web Token."""

        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-events', kwargs = {'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_contract_event_without_JWT(self):
        """Test the event listing by contract without a Json Web Token."""

        url = reverse('contracts-events', kwargs = {'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_modify_contract_status_as_management(self):
        """Test the contract status update as a management team member."""

        user = Staff.objects.get(username = 'StaffManagementA')
        self.client.force_authenticate(user)  

        url = reverse('contracts-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_contract_statut_as_sales_contact(self):
        """Test the contract status update as the sales contact."""

        user = Staff.objects.get(username = 'StaffSalesA')
        self.client.force_authenticate(user)  

        url = reverse('contracts-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["ContractStatutID"], 1)

    def test_modify_contract_statut_as_sales(self):
        """Test the contract status update as a sales team member who is not the sales 
        contact."""

        user = Staff.objects.get(username = 'StaffSalesB')
        self.client.force_authenticate(user)  

        url = reverse('contracts-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_contract_statut_as_support(self):
        """Test the contract status update as a support team member."""

        user = Staff.objects.get(username = 'StaffSupportA')
        self.client.force_authenticate(user)  

        url = reverse('contracts-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_modify_contract_statut_with_fake_JWT(self):
        """Test the contract status update with a fake Json Web Token."""

        token = 'Fake_Token'

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url = reverse('contracts-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_modify_contract_statut_without_JWT(self):
        """Test the contract status update without a Json Web Token."""

        url = reverse('contracts-change-status', kwargs = {'pk': 1})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_modify_contract_statut_already_actual(self):
        """Test the contract status update of a contract that already have the signed 
        status."""

        user = Staff.objects.get(username = 'StaffSalesA')
        self.client.force_authenticate(user)  

        url = reverse('contracts-change-status', kwargs = {'pk': 3})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
