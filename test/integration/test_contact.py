BASE_URL = "http://localhost:5000"

def setup_module(module):
    pass


def teardown_module(module):
    pass


def test_get_contacts(client):
    response = client.get(BASE_URL + "/api/contacts")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_contacts(client):
    """בדיקה: קריאת רשימת כל אנשי הקשר"""
    response = client.get(BASE_URL + "/api/contacts")
    
    # לוודא שהסטטוס הוא 200 (הצלחה)
    assert response.status_code == 200
    
    # לוודא שהתגובה היא רשימה
    assert isinstance(response.get_json(), list)
    
    # אפשר גם לוודא שיש לפחות איש קשר אחד
    assert len(response.get_json()) > 0

def test_delete_contact(client):
    contact_id = 101
    new_contact = {"name": "John Doe", "email": "john.doe@example.com", "phone": "1234567890"}
    response = client.post(f"{BASE_URL}/api/contacts", json=new_contact)
    assert response.status_code == 201


    response = client.delete(f"{BASE_URL}/api/contacts/{contact_id}")
    assert response.status_code == 204
    

    response_json = response.get_json()
    assert response_json is None  
    response = client.get(f"{BASE_URL}/api/contacts/{contact_id}")
    assert response.status_code == 404 

def test_get_and_delete_contact(client):
    contact_id = 101
    
    new_contact_data = {"name": "John Doe", "email": "john@example.com" ,"phone": "1234567890"}
    response = client.post(f"{BASE_URL}/api/contacts", json=new_contact_data)
    assert response.status_code == 201


    response = client.get(f"{BASE_URL}/api/contacts/{contact_id}")
    assert response.status_code == 200 

    contact_data = response.get_json()
    assert contact_data is not None
    assert contact_data['id'] == contact_id
    assert contact_data['name'] == "John Doe"
    assert contact_data['email'] == "john@example.com"


    response = client.delete(f"{BASE_URL}/api/contacts/{contact_id}")
    assert response.status_code == 204  

    response = client.get(f"{BASE_URL}/api/contacts/{contact_id}")
    assert response.status_code ==404 
    assert response.get_json() is None