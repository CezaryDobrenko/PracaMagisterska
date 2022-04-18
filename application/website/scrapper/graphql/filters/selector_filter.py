from django_filters import (
    BooleanFilter,
    FilterSet,
    OrderingFilter,
    CharFilter,
)
from graphene_django.filter import GlobalIDMultipleChoiceFilter

class SelectorFilter(FilterSet):
    order_by = OrderingFilter(
        fields=("created_date", "modified_date"),
    )

    value = CharFilter(lookup_expr="icontains", field_name="value")
    description = CharFilter(lookup_expr="icontains", field_name="description")
    selector_type = GlobalIDMultipleChoiceFilter()

    def is_ready_filter(self, queryset, name, value):
        if value:
            return queryset.filter(is_ready=True)
        return queryset.filter(is_ready=False)