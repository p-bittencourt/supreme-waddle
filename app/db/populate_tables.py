from app.db.database import Base, engine
from app.models.user import User

users = [
    {"name": "Mark Johnson", "email": "mark@email.com"},
    {"name": "Sarah Williams", "email": "sarah.w@company.org"},
    {"name": "Alex Rodriguez", "email": "arod@example.com"},
    {"name": "Priya Patel", "email": "priya.patel@gmail.com"},
    {"name": "John Smith", "email": "jsmith@business.net"},
    {"name": "Olivia Chen", "email": "olivia.c@techinc.com"},
    {"name": "Mohammed Al-Farsi", "email": "m.alfarsi@consultancy.co"},
    {"name": "Aisha Washington", "email": "a.washington@university.edu"},
    {"name": "Carlos Rodriguez", "email": "carlos.r@startup.io"},
    {"name": "Emma Davies", "email": "emma.d@research.org"},
]


def populate_users():
    pass
