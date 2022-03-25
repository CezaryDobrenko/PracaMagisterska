from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, DetailView, FormView, ListView, UpdateView, TemplateView
from scrapper.models.folder import Folder
from scrapper.models.website import Website




class LoginView(LoginRequiredMixin, TemplateView):
    template_name = "scrapper/login.html"


class StatisticView(LoginRequiredMixin, TemplateView):
    template_name = "scrapper/statistics.html"


class PrivateDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "scrapper/private_dashboard.html"
