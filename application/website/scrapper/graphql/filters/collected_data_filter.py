from django_filters import (
    BooleanFilter,
    FilterSet,
    OrderingFilter,
    CharFilter,
)
from graphene_django.filter import GlobalIDMultipleChoiceFilter

class CollectedDataFilter(FilterSet):
    order_by = OrderingFilter(
        fields=("created_date", "modified_date"),
    )

    value = CharFilter(lookup_expr="icontains", field_name="value")