# Justin Ventura

# Imports for database seeding:
from .models import UserModel
from api import db

# Seed testing data:
me = UserModel(id=1,
                username='jventura3', 
                email='jventura3@gulls.salisbury.edu',
                password='a900a10c4d321f8338325b3cea14cbaa53a87bd3462bac578ab3966ea7ab9db8')

db.session.add(me)
db.session.commit()
