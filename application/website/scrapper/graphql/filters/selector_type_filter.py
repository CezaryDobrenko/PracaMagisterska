from django_filters import (
    BooleanFilter,
    FilterSet,
    OrderingFilter,
    CharFilter,
)
from graphene_django.filter import GlobalIDMultipleChoiceFilter

class SelectorTypeFilter(FilterSet):
    order_by = OrderingFilter(
        fields=("created_date", "modified_date"),
    )

    name = CharFilter(lookup_expr="icontains", field_name="name")
    description = CharFilter(lookup_expr="icontains", field_name="description")