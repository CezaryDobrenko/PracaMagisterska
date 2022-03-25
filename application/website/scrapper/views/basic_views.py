from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = "scrapper/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_authorized'] = 1
        return context


class AboutView(TemplateView):
    template_name = "scrapper/about.html"


class ContactView(TemplateView):
    template_name = "scrapper/contact.html"


class ProcessView(TemplateView):
    template_name = "scrapper/how_it_works.html"


class AuthorView(TemplateView):
    template_name = "scrapper/author.html"


class MissionView(TemplateView):
    template_name = "scrapper/mission.html"

class RegisterView(LoginRequiredMixin, TemplateView):
    template_name = "scrapper/register.html"
