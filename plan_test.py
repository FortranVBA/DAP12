

#def test_succeed_authentification(client):
#    response = client.post('/login/', data={"UserName":"StaffGestionA"})
#    assert response.status_code == 200
#    assert b"JWT" in response.data


def test_failed_authentification(client):
    response = client.post('/login/', data={"UserName":"UnknownUser"})
    assert response.status_code == 200
    assert b"Error" in response.data

def test_add_user_as_management(client):
    response = client.post('/login/', data={"UserName":"StaffGestionA"})
    JWT = response.JWT

    response = client.post('/users/', data={"CompanyName":"NewCompany", 
    "StaffProfile":"Vente"}, JWT=JWT)
    assert response.status_code == 201
    assert b"NewCompany" in response.data
    assert b"Vente" in response.data

def test_add_user_as_sales(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.post('/users/', data={"CompanyName":"NewCompany"}, JWT=JWT)
    assert response.status_code == 200
    assert b"Error" in response.data

def test_add_user_as_support(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.post('/users/', data={"CompanyName":"NewCompany"}, JWT=JWT)
    assert response.status_code == 200
    assert b"Error" in response.data

def test_add_user_with_fake_JWT(client):
    JWT = "FakeJWT"

    response = client.post('/users/', data={"CompanyName":"NewCompany"}, JWT=JWT)
    assert response.status_code == 200
    assert b"Error" in response.data

def test_add_user_without_JWT(client):
    response = client.post('/users/', data={"CompanyName":"NewCompany"})
    assert response.status_code == 200
    assert b"Error" in response.data

def test_delete_user_as_management(client):
    response = client.post('/login/', data={"UserName":"StaffGestionA"})
    JWT = response.JWT

    response = client.delete('/users/1/')
    assert response.status_code == 204

def test_delete_user_as_sales(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.delete('/users/1/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_delete_user_as_support(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.delete('/users/1/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_delete_user_with_fake_JWT(client):
    JWT = "FakeJWT"

    response = client.delete('/users/1/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_delete_user_without_JWT(client):
    response = client.delete('/users/1/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_list_user_as_management(client):
    response = client.post('/login/', data={"UserName":"StaffGestionA"})
    JWT = response.JWT

    response = client.get('/users/')
    assert response.status_code == 200
    assert b"StaffGestionA" in response.data
    assert b"StaffGestionB" in response.data
    assert b"StaffVenteA" in response.data

def test_list_user_as_sales(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.get('/users/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_list_user_as_support(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.get('/users/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_list_user_with_fake_JWT(client):
    JWT = "FakeJWT"

    response = client.get('/users/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_list_user_without_JWT(client):
    response = client.get('/users/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_user_as_management(client):
    response = client.post('/login/', data={"UserName":"StaffGestionA"})
    JWT = response.JWT

    response = client.patch('/users/1/', data={"UserName":"StaffGestionC"})
    assert response.status_code == 200
    assert b"StaffGestionC" in response.data

def test_modify_user_as_sales(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.patch('/users/1/', data={"UserName":"StaffGestionC"})
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_user_as_support(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.patch('/users/1/', data={"UserName":"StaffGestionC"})
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_user_with_fake_JWT(client):
    JWT = "FakeJWT"

    response = client.patch('/users/1/', data={"UserName":"StaffGestionC"})
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_user_without_JWT(client):
    response = client.patch('/users/1/', data={"UserName":"StaffGestionC"})
    assert response.status_code == 200
    assert b"Error" in response.data



def test_list_client_as_management(client):
    response = client.post('/login/', data={"UserName":"StaffGestionA"})
    JWT = response.JWT

    response = client.get('/clients/')
    assert response.status_code == 200
    assert b"ClientA" in response.data
    assert b"ClientB" in response.data
    assert b"ClientC" in response.data

def test_list_client_as_sales(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.get('/clients/')
    assert response.status_code == 200
    assert b"ClientA" in response.data
    assert b"ClientB" in response.data
    assert b"ClientC" in response.data

def test_list_client_as_support(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.get('/clients/')
    assert response.status_code == 200
    assert b"ClientA" in response.data
    assert b"ClientB" in response.data
    assert b"ClientC" in response.data

def test_list_client_with_fake_JWT(client):
    JWT = "FakeJWT"

    response = client.get('/clients/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_list_client_without_JWT(client):
    response = client.get('/clients/')
    assert response.status_code == 200
    assert b"Error" in response.data



def test_add_client_as_management(client):
    response = client.post('/login/', data={"UserName":"StaffGestionA"})
    JWT = response.JWT

    response = client.post('/clients/', data={"CompanyName":"NewCompany"}, JWT=JWT)
    assert response.status_code == 200
    assert b"Error" in response.data

def test_add_client_as_sales(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.post('/clients/', data={"CompanyName":"NewCompany"}, JWT=JWT)
    assert response.status_code == 201
    assert b"NewCompany" in response.data

def test_add_client_as_support(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.post('/clients/', data={"CompanyName":"NewCompany"}, JWT=JWT)
    assert response.status_code == 200
    assert b"Error" in response.data

def test_add_client_with_fake_JWT(client):
    JWT = "FakeJWT"

    response = client.post('/clients/', data={"CompanyName":"NewCompany"}, JWT=JWT)
    assert response.status_code == 200
    assert b"Error" in response.data

def test_add_client_without_JWT(client):
    response = client.post('/clients/', data={"CompanyName":"NewCompany"}, JWT=JWT)
    assert response.status_code == 200
    assert b"Error" in response.data



def test_modify_client_as_management(client):
    response = client.post('/login/', data={"UserName":"StaffGestionA"})
    JWT = response.JWT

    response = client.patch('/clients/1/', data={"CompanyName":"ClientD"})
    assert response.status_code == 200
    assert b"ClientD" in response.data

def test_modify_client_as_sales_contact(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.patch('/clients/1/', data={"CompanyName":"ClientD"})
    assert response.status_code == 200
    assert b"ClientD" in response.data

def test_modify_client_as_sales(client):
    response = client.post('/login/', data={"UserName":"StaffVenteB"})
    JWT = response.JWT

    response = client.patch('/clients/1/', data={"CompanyName":"ClientD"})
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_client_as_support(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.patch('/clients/1/', data={"CompanyName":"ClientD"})
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_client_with_fake_JWT(client):
    JWT = "FakeJWT"

    response = client.patch('/clients/1/', data={"CompanyName":"ClientD"})
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_client_without_JWT(client):
    response = client.patch('/clients/1/', data={"CompanyName":"ClientD"})
    assert response.status_code == 200
    assert b"Error" in response.data



def test_modify_client_statut_as_management(client):
    response = client.post('/login/', data={"UserName":"StaffGestionA"})
    JWT = response.JWT

    response = client.post('/clients/1/change_status/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_client_statut_as_sales_contact(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.post('/clients/1/change_status/')
    assert response.status_code == 200
    assert b"Actual" in response.data

def test_modify_client_statut_as_sales(client):
    response = client.post('/login/', data={"UserName":"StaffVenteB"})
    JWT = response.JWT

    response = client.post('/clients/1/change_status/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_client_statut_as_support(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.post('/clients/1/change_status/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_client_statut_with_fake_JWT(client):
    JWT = "FakeJWT"

    response = client.post('/clients/1/change_status/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_client_statut_without_JWT(client):
    response = client.post('/clients/1/change_status/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_client_statut__already_actual(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.post('/clients/3/change_status/')
    assert response.status_code == 200
    assert b"Error" in response.data



def test_list_contract_as_management(client):
    response = client.post('/login/', data={"UserName":"StaffGestionA"})
    JWT = response.JWT

    response = client.get('/contracts/')
    assert response.status_code == 200
    assert b"ClientA" in response.data
    assert b"ClientB" in response.data
    assert b"ClientC" in response.data
    assert b"Amount" in response.data
    assert b"9050" in response.data
    assert b"500.59" in response.data
    assert b"900" in response.data

def test_list_contract_as_sales(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.get('/contracts/')
    assert response.status_code == 200
    assert b"ClientA" in response.data
    assert b"ClientB" in response.data
    assert b"ClientC" in response.data
    assert b"Amount" in response.data
    assert b"9050" in response.data
    assert b"500.59" in response.data
    assert b"900" in response.data

def test_list_contract_as_support(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.get('/contracts/')
    assert response.status_code == 200
    assert b"ClientA" in response.data
    assert b"ClientB" in response.data
    assert b"ClientC" in response.data
    assert b"Amount" in response.data
    assert b"9050" in response.data
    assert b"500.59" in response.data
    assert b"900" in response.data

def test_list_contract_with_fake_JWT(client):
    JWT = "FakeJWT"

    response = client.get('/contracts/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_list_contract_without_JWT(client):
    response = client.get('/contracts/')
    assert response.status_code == 200
    assert b"Error" in response.data



def test_modify_contract_as_management(client):
    response = client.post('/login/', data={"UserName":"StaffGestionA"})
    JWT = response.JWT

    response = client.patch('/contracts/1/', data={"Amount":"88"})
    assert response.status_code == 200
    assert b"88" in response.data

def test_modify_contract_as_sales_contact(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.patch('/contracts/1/', data={"Amount":"88"})
    assert response.status_code == 200
    assert b"88" in response.data

def test_modify_contract_as_sales(client):
    response = client.post('/login/', data={"UserName":"StaffVenteB"})
    JWT = response.JWT

    response = client.patch('/contracts/1/', data={"Amount":"88"})
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_contract_as_support(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.patch('/contracts/1/', data={"Amount":"88"})
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_contract_with_fake_JWT(client):
    JWT = "FakeJWT"

    response = client.patch('/contracts/1/', data={"Amount":"88"})
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_contract_without_JWT(client):
    response = client.patch('/contracts/1/', data={"Amount":"88"})
    assert response.status_code == 200
    assert b"Error" in response.data



def test_modify_contract_statut_as_management(client):
    response = client.post('/login/', data={"UserName":"StaffGestionA"})
    JWT = response.JWT

    response = client.post('/contracts/1/change_status/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_contract_statut_as_sales_contact(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.post('/contracts/1/change_status/')
    assert response.status_code == 200
    assert b"Signed" in response.data

def test_modify_contract_statut_as_sales(client):
    response = client.post('/login/', data={"UserName":"StaffVenteB"})
    JWT = response.JWT

    response = client.post('/contracts/1/change_status/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_contract_statut_as_support(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.post('/contracts/1/change_status/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_contract_statut_with_fake_JWT(client):
    JWT = "FakeJWT"

    response = client.post('/contracts/1/change_status/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_contract_statut_without_JWT(client):
    response = client.post('/contracts/1/change_status/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_contract_statut__already_actual(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.post('/contracts/3/change_status/')
    assert response.status_code == 200
    assert b"Error" in response.data




def test_add_contract_as_management(client):
    response = client.post('/login/', data={"UserName":"StaffGestionA"})
    JWT = response.JWT

    response = client.post('/contracts/', data={"Client":"ClientA", 
    "Amount":"500.59"}, JWT=JWT)
    assert response.status_code == 200
    assert b"Error" in response.data

def test_add_contract_as_sales(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.post('/contracts/', data={"Client":"ClientA", 
    "Amount":"500.59"}, JWT=JWT)
    assert response.status_code == 201
    assert b"ClientA" in response.data
    assert b"500.59" in response.data

def test_add_contract_as_support(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.post('/contracts/', data={"Client":"ClientA", 
    "Amount":"500.59"}, JWT=JWT)
    assert response.status_code == 200
    assert b"Error" in response.data

def test_add_contract_with_fake_JWT(client):
    JWT = "FakeJWT"

    response = client.post('/contracts/', data={"Client":"ClientA", 
    "Amount":"500.59"}, JWT=JWT)
    assert response.status_code == 200
    assert b"Error" in response.data

def test_add_contract_without_JWT(client):
    response = client.post('/contracts/', data={"Client":"ClientA", 
    "Amount":"500.59"}, JWT=JWT)
    assert response.status_code == 200
    assert b"Error" in response.data



def test_list_contract_event_as_management(client):
    response = client.post('/login/', data={"UserName":"StaffGestionA"})
    JWT = response.JWT

    response = client.get('/contracts/1/events/')
    assert response.status_code == 200
    assert b"90" in response.data
    assert b"50" in response.data
    assert b"11" not in response.data

def test_list_contract_event_as_sales(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.get('/contracts/1/events/')
    assert response.status_code == 200
    assert b"90" in response.data
    assert b"50" in response.data
    assert b"11" not in response.data

def test_list_contract_event_as_support(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.get('/contracts/1/events/')
    assert response.status_code == 200
    assert b"90" in response.data
    assert b"50" in response.data
    assert b"11" not in response.data

def test_list_contract_event_with_fake_JWT(client):
    JWT = "FakeJWT"

    response = client.get('/contracts/1/events/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_list_contract_event_without_JWT(client):
    response = client.get('/contracts/1/events/')
    assert response.status_code == 200
    assert b"Error" in response.data



def test_list_event_as_management(client):
    response = client.post('/login/', data={"UserName":"StaffGestionA"})
    JWT = response.JWT

    response = client.get('/events/')
    assert response.status_code == 200
    assert b"90" in response.data
    assert b"50" in response.data
    assert b"11" in response.data

def test_list_event_as_sales(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.get('/events/')
    assert response.status_code == 200
    assert b"90" in response.data
    assert b"50" in response.data
    assert b"11" in response.data

def test_list_event_as_support(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.get('/events/')
    assert response.status_code == 200
    assert b"90" in response.data
    assert b"50" in response.data
    assert b"11" in response.data

def test_list_event_with_fake_JWT(client):
    JWT = "FakeJWT"

    response = client.get('/events/')
    assert response.status_code == 200
    assert b"Error" in response.data

def test_list_event_without_JWT(client):
    response = client.get('/events/')
    assert response.status_code == 200
    assert b"Error" in response.data



def test_add_event_as_management(client):
    response = client.post('/login/', data={"UserName":"StaffGestionA"})
    JWT = response.JWT

    response = client.post('/events/', data={"Contract":"Contract ClientC"}, JWT=JWT)
    assert response.status_code == 200
    assert b"Error" in response.data

def test_add_event_as_sales(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.post('/events/', data={"Contract":"Contract ClientC"}, JWT=JWT)
    assert response.status_code == 201
    assert b"Contract ClientC" in response.data

def test_add_event_as_support(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.post('/events/', data={"Contract":"Contract ClientC"}, JWT=JWT)
    assert response.status_code == 200
    assert b"Error" in response.data

def test_add_event_with_fake_JWT(client):
    JWT = "FakeJWT"

    response = client.post('/events/', data={"Contract":"Contract ClientC"}, JWT=JWT)
    assert response.status_code == 200
    assert b"Error" in response.data

def test_add_event_without_JWT(client):
    response = client.post('/events/', data={"Contract":"Contract ClientC"}, JWT=JWT)
    assert response.status_code == 200
    assert b"Error" in response.data



def test_modify_event_as_management(client):
    response = client.post('/login/', data={"UserName":"StaffGestionA"})
    JWT = response.JWT

    response = client.patch('/events/1/', data={"Attendees":"88"})
    assert response.status_code == 200
    assert b"88" in response.data

def test_modify_event_as_sales_contact(client):
    response = client.post('/login/', data={"UserName":"StaffVenteA"})
    JWT = response.JWT

    response = client.patch('/events/1/', data={"Attendees":"88"})
    assert response.status_code == 200
    assert b"88" in response.data

def test_modify_event_as_sales(client):
    response = client.post('/login/', data={"UserName":"StaffVenteB"})
    JWT = response.JWT

    response = client.patch('/events/1/', data={"Attendees":"88"})
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_event_as_support_contact(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.patch('/events/1/', data={"Attendees":"88"})
    assert response.status_code == 200
    assert b"88" in response.data

def test_modify_event_as_support(client):
    response = client.post('/login/', data={"UserName":"SupportA"})
    JWT = response.JWT

    response = client.patch('/events/1/', data={"Attendees":"88"})
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_event_with_fake_JWT(client):
    JWT = "FakeJWT"

    response = client.patch('/events/1/', data={"Attendees":"88"})
    assert response.status_code == 200
    assert b"Error" in response.data

def test_modify_event_without_JWT(client):
    response = client.patch('/events/1/', data={"Attendees":"88"})
    assert response.status_code == 200
    assert b"Error" in response.data
