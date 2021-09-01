

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


