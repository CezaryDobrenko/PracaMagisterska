import logging
import graphene



logger = logging.getLogger(__name__)

class TestMutation(graphene.Mutation):
    test = graphene.Int()

    class Arguments:
        argum = graphene.Int(required=True)

    def mutate(self, info, argum: int):
        return TestMutation(test=argum)

class UserMutation(graphene.ObjectType):
    test_mutation = TestMutation.Field()
