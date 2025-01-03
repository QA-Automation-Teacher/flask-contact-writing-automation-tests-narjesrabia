# conftest.py
import pytest
from app import app  # ייבא את האפליקציה שלך

@pytest.fixture
def client():
    with app.test_client() as client:  # יוצר אובייקט client שמחובר לאפליקציה שלך
        yield client  # מחזיר את ה-client לשימוש בבדיקות
