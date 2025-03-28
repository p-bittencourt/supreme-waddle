"""Sample data to be used for populating db"""

from app.schemas.expense import ExpenseCategory


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

expenses = [
    # User 1: Mark Johnson
    {
        "title": "Weekly grocery shopping",
        "category": ExpenseCategory.GROCERIES,
        "value": 87.34,
        "user_id": 1,
    },
    {
        "title": "Netflix subscription",
        "category": ExpenseCategory.SUBSCRIPTIONS,
        "value": 15.99,
        "user_id": 1,
    },
    {
        "title": "Gas refill",
        "category": ExpenseCategory.TRANSPORTATION,
        "value": 45.50,
        "user_id": 1,
    },
    # User 2: Sarah Williams
    {
        "title": "Rent payment",
        "category": ExpenseCategory.HOUSING,
        "value": 1200.00,
        "user_id": 2,
    },
    {
        "title": "Electric bill",
        "category": ExpenseCategory.UTILITIES,
        "value": 85.43,
        "user_id": 2,
    },
    # User 3: Alex Rodriguez
    {
        "title": "Gym membership",
        "category": ExpenseCategory.HEALTH,
        "value": 49.99,
        "user_id": 3,
    },
    {
        "title": "Birthday dinner",
        "category": ExpenseCategory.DINING,
        "value": 78.25,
        "user_id": 3,
    },
    {
        "title": "Amazon Prime",
        "category": ExpenseCategory.SUBSCRIPTIONS,
        "value": 14.99,
        "user_id": 3,
    },
    # User 4: Priya Patel
    {
        "title": "Online course",
        "category": ExpenseCategory.EDUCATION,
        "value": 199.99,
        "user_id": 4,
    },
    {
        "title": "Work clothes",
        "category": ExpenseCategory.CLOTHING,
        "value": 156.78,
        "user_id": 4,
    },
    # User 5: John Smith
    {
        "title": "Car insurance",
        "category": ExpenseCategory.INSURANCE,
        "value": 112.50,
        "user_id": 5,
    },
    {
        "title": "Internet bill",
        "category": ExpenseCategory.UTILITIES,
        "value": 65.00,
        "user_id": 5,
    },
    {
        "title": "Pharmacy",
        "category": ExpenseCategory.HEALTH,
        "value": 32.47,
        "user_id": 5,
    },
    # User 6: Olivia Chen
    {
        "title": "Weekend trip",
        "category": ExpenseCategory.TRAVEL,
        "value": 325.68,
        "user_id": 6,
    },
    {
        "title": "Restaurant with friends",
        "category": ExpenseCategory.DINING,
        "value": 86.42,
        "user_id": 6,
    },
    # User 7: Mohammed Al-Farsi
    {
        "title": "Monthly savings",
        "category": ExpenseCategory.SAVINGS,
        "value": 500.00,
        "user_id": 7,
    },
    {
        "title": "Water bill",
        "category": ExpenseCategory.UTILITIES,
        "value": 42.15,
        "user_id": 7,
    },
    {
        "title": "Home repairs",
        "category": ExpenseCategory.HOUSING,
        "value": 237.50,
        "user_id": 7,
    },
    # User 8: Aisha Washington
    {
        "title": "Textbooks",
        "category": ExpenseCategory.EDUCATION,
        "value": 215.30,
        "user_id": 8,
    },
    {
        "title": "Phone bill",
        "category": ExpenseCategory.UTILITIES,
        "value": 89.99,
        "user_id": 8,
    },
    # User 9: Carlos Rodriguez
    {
        "title": "Mother's day gift",
        "category": ExpenseCategory.GIFTS,
        "value": 75.00,
        "user_id": 9,
    },
    {
        "title": "Movie tickets",
        "category": ExpenseCategory.ENTERTAINMENT,
        "value": 28.50,
        "user_id": 9,
    },
    {
        "title": "Haircut",
        "category": ExpenseCategory.PERSONAL,
        "value": 45.00,
        "user_id": 9,
    },
    # User 10: Emma Davies
    {
        "title": "Monthly bus pass",
        "category": ExpenseCategory.TRANSPORTATION,
        "value": 65.00,
        "user_id": 10,
    },
    {
        "title": "Office supplies",
        "category": ExpenseCategory.MISCELLANEOUS,
        "value": 23.42,
        "user_id": 10,
    },
]
