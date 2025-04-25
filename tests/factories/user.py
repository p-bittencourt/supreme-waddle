"""Factory for users"""

import factory
from app.models.user import User


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    """User Factory"""

    class Meta:
        model = User  # SQLAlchemy model
        sqlalchemy_session_persistence = (
            "commit"  # Commit the session after creating the user instance
        )

    name = factory.Faker("name")
    email = factory.Faker("email")
