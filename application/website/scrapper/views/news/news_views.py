from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, FormView
from scrapper.models.folder import Folder
from scrapper.models.website import Website
from .news_forms import NewsClearForm
from django.urls import reverse_lazy

class NewsList(LoginRequiredMixin, ListView):
    model = Website
    template_name = "scrapper/news/news_list.html"
    paginate_by = 10
    ordering = ['pk']

    def get_queryset(self):
        websites = []
        for folder in Folder.objects.filter(user_id=self.request.user.id, is_ready=True):
            for website in Website.objects.filter(folder_id=folder.id, is_new_data_collected=True):
                websites.append(website)
        return websites


class NewsClear(LoginRequiredMixin, FormView):
    form_class = NewsClearForm
    template_name = "scrapper/news/news_clear.html"
    success_url = reverse_lazy("news")

    def form_valid(self, form):
        id = self.request.resolver_match.kwargs.get("pk")
        form.save(id)
        return super().form_valid(form)