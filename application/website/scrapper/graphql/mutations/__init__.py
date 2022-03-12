import graphene
import graphql_jwt

from scrapper.graphql.mutations.user import UserMutation


class Mutation(
    UserMutation,
    graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
