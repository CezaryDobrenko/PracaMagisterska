from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from .timezone_forms import ChangeTimezoneForm
from django.urls import reverse_lazy
from scrapper.models.timezone import Timezone

class ChangeTimezone(LoginRequiredMixin, FormView):
    form_class = ChangeTimezoneForm
    template_name = "scrapper/timezone/change_timezone.html"
    success_url = reverse_lazy("private_dashboard")

    def form_valid(self, form):
        id = self.request.resolver_match.kwargs.get("pk")
        form.save(id)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        timezones = Timezone.objects.all()
        context["timezones"] = timezones
        return context