from models import db, Contacts
from faker import Factory
from app import app

with app.app_context():

    fake = Factory.create()

    fake = Factory.create('ar_PS')

    db.drop_all()
    db.create_all()
 
    for num in range(100):
        fullname = fake.name().split()
        name = fullname[0]
        surname = ' '.join(fullname[1:])
        email = fake.email()
        phone = fake.phone_number()
   
        mi_contacto = Contacts(name, surname, email, phone)
        db.session.add(mi_contacto)
        db.session.commit()
