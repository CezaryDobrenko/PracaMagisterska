from scrapper.views.basic_forms import BaseForm
from scrapper.models.folder import Folder
from scrapper.models.website import Website
from django.urls import reverse
from django.http import HttpResponseRedirect

class NewsClearForm(BaseForm):
    class Meta:
        model = Website
        fields = []

    def save(self, id, commit=True):
        for folder in Folder.objects.filter(user_id=id, is_ready=True):
            for website in Website.objects.filter(folder_id=folder.id, is_new_data_collected=True):
                website.update_is_new_data_collected(False)
        return HttpResponseRedirect(reverse('news'))