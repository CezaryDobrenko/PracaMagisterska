from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, FormView, ListView
from scrapper.models.folder import Folder
from scrapper.models.website import Website
from django.urls import reverse_lazy
from scrapper.translations.language_pl import FolderTranslator
from scrapper.models.utils.intervals import Interval

class FoldersList(LoginRequiredMixin, ListView):
    model = Folder
    template_name = "scrapper/folder/folders_list.html"
    paginate_by = 20
    ordering = ['pk']

    def get_queryset(self):
        folders = []
        for folder in Folder.objects.filter(user_id=self.request.user.id):
            next_scraping_date = Interval.find_next_scraping_date(folder.last_scraping, folder.scraping_interval)
            folder.sites = Website.objects.filter(folder_id=folder.id).count()
            folder.is_ready = FolderTranslator.is_ready_to_pl(folder.is_ready)
            folder.scraping_interval = FolderTranslator.interval_to_pl(folder.scraping_interval)
            folder.last_scraping = FolderTranslator.scraping_date_to_pl(folder.last_scraping)
            folder.next_scraping = FolderTranslator.scraping_date_to_pl(next_scraping_date)
            folders.append(folder)
        return folders

class FoldersDelete(LoginRequiredMixin, DeleteView):
    model = Folder
    template_name = "scrapper/folder/folders_delete.html"
    success_url = reverse_lazy("folders")