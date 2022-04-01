from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, ListView, FormView, UpdateView
from scrapper.models.website import Website
from scrapper.models.selectors import Selector
from scrapper.translations.language_pl import Translator
from .website_forms import WebsiteCreateForm, WebsiteUpdateForm, WebsiteClearForm
from django.urls import reverse_lazy, reverse


class WebsitesList(LoginRequiredMixin, ListView):
    model = Website
    template_name = "scrapper/website/webistes_list.html"
    paginate_by = 20
    ordering = ['pk']

    def get_queryset(self):
        folder_id = self.request.resolver_match.kwargs.get("pk")
        websites = []
        for website in Website.objects.filter(folder_id=folder_id):
            website.is_ready = Translator.is_ready_to_pl(website.is_ready)
            website.selectors = Selector.objects.filter(website_id=website.id).count()
            websites.append(website)
        return websites

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["folder_id"] = self.request.resolver_match.kwargs.get("pk")
        return context


class WebsitesDelete(LoginRequiredMixin, DeleteView):
    model = Website
    template_name = "scrapper/website/websites_delete.html"

    def get_success_url(self):
        website_id = self.kwargs["pk"]
        website = Website.objects.filter(id=website_id).first()
        return reverse("websites-settings", kwargs={"pk": website.folder.id})


class WebsitesClear(LoginRequiredMixin, FormView):
    form_class = WebsiteClearForm
    template_name = "scrapper/website/websites_clear.html"

    def form_valid(self, form):
        folder_id = self.request.resolver_match.kwargs.get("pk")
        form.cleaned_data["folder_id"] = folder_id
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("websites-settings", kwargs={"pk": self.kwargs["pk"]})


class WebsiteCreate(LoginRequiredMixin, FormView):
    form_class = WebsiteCreateForm
    template_name = "scrapper/website/websites_add.html"

    def form_valid(self, form):
        folder_id = self.request.resolver_match.kwargs.get("pk")
        form.cleaned_data["folder_id"] = folder_id
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("websites-settings", kwargs={"pk": self.kwargs["pk"]})


class WebsiteUpdate(LoginRequiredMixin, UpdateView):
    model = Website
    form_class = WebsiteUpdateForm
    template_name = "scrapper/website/websites_update.html"

    def form_valid(self, form):
        folder_id = self.request.resolver_match.kwargs.get("pk")
        form.cleaned_data["folder_id"] = folder_id
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        website_id = self.kwargs["pk"]
        website = Website.objects.filter(id=website_id).first()
        return reverse("websites-settings", kwargs={"pk": website.folder.id})