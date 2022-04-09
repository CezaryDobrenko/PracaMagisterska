from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(TemplateView):
    template_name = "scrapper/dashboard.html"


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


class PrivateDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "scrapper/private_dashboard.html"