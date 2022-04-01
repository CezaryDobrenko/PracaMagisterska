from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView
from scrapper.models.collected_data import CollectedData
from scrapper.models.selectors import Selector
from django.urls import reverse


class CollectedDataList(LoginRequiredMixin, ListView):
    model = CollectedData
    template_name = "scrapper/collected_data/data_list.html"
    paginate_by = 20
    ordering = ['pk']

    def get_queryset(self):
        selector_id = self.request.resolver_match.kwargs.get("pk")
        return CollectedData.objects.filter(selector_id=selector_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selector_id = self.request.resolver_match.kwargs.get("pk")
        selector = Selector.objects.filter(id=selector_id).first()
        context["return_id"] = selector.website.id
        return context


class CollectedDataDelete(LoginRequiredMixin, DeleteView):
    model = CollectedData
    template_name = "scrapper/collected_data/data_delete.html"

    def get_success_url(self):
        data_id = self.kwargs["pk"]
        collected_data = CollectedData.objects.filter(id=data_id).first()
        return reverse("collected-data-list", kwargs={"pk": collected_data.selector.id})
