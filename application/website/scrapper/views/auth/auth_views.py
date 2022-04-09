from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .auth_forms import RegisterForm


class LoginView(LoginRequiredMixin, TemplateView):
    template_name = "scrapper/auth/login.html"


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "scrapper/auth/register.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.cleaned_data["email"] = form.data["username"]
        form.cleaned_data["password"] = form.data["password"]
        form.cleaned_data["password2"] = form.data["password2"]
        form.save()
        return super().form_valid(form)