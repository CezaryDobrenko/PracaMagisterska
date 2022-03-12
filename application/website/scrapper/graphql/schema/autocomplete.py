import graphene
from graphene.relay.node import to_global_id

class Autocomplete(graphene.ObjectType):
    id = graphene.ID()
    test = graphene.Boolean()

    def resolve_test(self, info, **args):
        return True
    

autocomplete_instance = Autocomplete(id=to_global_id("Autocomplete", 1))


class AutocompleteQuery(graphene.ObjectType):
    autocomplete = graphene.Field(Autocomplete)

    def resolve_autocomplete(self, info):
        return autocomplete_instance
