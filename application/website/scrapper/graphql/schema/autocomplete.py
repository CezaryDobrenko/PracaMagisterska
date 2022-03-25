import graphene
from graphene.relay.node import to_global_id

class Autocomplete(graphene.ObjectType):
    id = graphene.ID()
    test = graphene.Boolean()

    def resolve_test(self, info, **args):
        return True
    
class AutocompleteQuery(graphene.ObjectType):
    autocomplete = graphene.Field(Autocomplete)

    def resolve_autocomplete(self, info):
        return Autocomplete(id=to_global_id("Autocomplete", 1))
