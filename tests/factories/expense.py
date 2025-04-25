"""Factory for Expenses"""

import random
import factory
from app.models.expense import Expense
from app.schemas.expense import ExpenseCategory
from tests.factories.user import UserFactory


class ExpenseFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Expense factory"""

    class Meta:
        model = Expense
        sqlalchemy_session_persistence = "commit"

    title = factory.Faker("sentence", nb_words=3)
    category = factory.LazyFunction(lambda: random.choice(list(ExpenseCategory)))
    value = factory.Faker("pyfloat", positive=True, right_digits=2, max_value=1000)
    user = factory.SubFactory(UserFactory)
