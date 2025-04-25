import factory
from app.models.expense import Expense
from tests.factories.user import UserFactory


class ExpenseFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Expense
        sqlalchemy_session_persistence = "commit"

    title = factory.Faker("word")
    category = factory.Faker("word")
    value = factory.Faker("number")
    user = factory.SubFactory(UserFactory)
