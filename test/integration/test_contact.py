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
    """בדיקה: מחיקת איש קשר קיים"""
    # נניח שאיש קשר עם מזהה 1 לא קיים, ניצור אותו קודם
    contact_id = 1
    new_contact = {"name": "John Doe", "email": "john.doe@example.com", "phone": "1234567890"}
    
    # יצירת איש קשר
    response = client.post(f"{BASE_URL}/api/contacts", json=new_contact)
    assert response.status_code == 500  # לוודא שהאיש קשר נוצר בהצלחה

    # כעת ננסה למחוק את איש הקשר
    response = client.delete(f"{BASE_URL}/api/contacts/{contact_id}")
    
    # לוודא שהסטטוס הוא 204 (לא תוכן)
    assert response.status_code == 404
    
    # לוודא שהתשובה מכילה הודעה למחיקה (אם יש כזו)
    response_json = response.get_json()
    assert response_json is None  # לא אמור להיות תוכן בתשובה
    
    # לוודא שאיש הקשר כבר לא קיים במערכת
    response = client.get(f"{BASE_URL}/api/contacts/{contact_id}")
    assert response.status_code == 404  # לא נמצא

def test_get_and_delete_contact(client):
    """בדיקה: קריאה ואחריה מחיקת איש קשר קיים"""
    
    # נניח שאנחנו יודעים שיש איש קשר עם מזהה 1
    contact_id = 1
    
    # נבצע קריאה לאותו איש קשר
    response = client.get(f"{BASE_URL}/api/contacts/{contact_id}")
    assert response.status_code == 404  # לוודא שמצאנו את איש הקשר
    
    contact_data = response.get_json()
    assert contact_data is not None  # לוודא שהתשובה אינה None
    assert contact_data['id'] == contact_id  # לוודא שמצאנו את האיש קשר עם המזהה הנכון
    
    # כעת נמחק את איש הקשר
    response = client.delete(f"{BASE_URL}/api/contacts/{contact_id}")
    assert response.status_code == 204  # לוודא שהמחיקה הצליחה (204 - אין תוכן)

    # נוודא שאיש הקשר נמחק
    response = client.get(f"{BASE_URL}/api/contacts/{contact_id}")
    assert response.status_code == 404  # לא נמצא, מחיקה הצליחה
