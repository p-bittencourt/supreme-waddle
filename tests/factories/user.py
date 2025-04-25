import factory
from app.models.user import User


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User  # SQLAlchemy model
        sqlalchemy_session_persistence = (
            "commit"  # Commit the session after creating the user instance
        )

    name = factory.Faker("name")
    email = factory.Faker("email")

    @classmethod
    def _create(cls, model_class):
        return super()._create(model_class)
