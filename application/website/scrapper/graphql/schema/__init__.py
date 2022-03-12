from graphene import Node

from scrapper.graphql.schema.autocomplete import AutocompleteQuery

class Query(AutocompleteQuery):
    node = Node.Field()
