from scrapper.views.basic_forms import BaseForm
from scrapper.models.website import Website
from django.utils.translation import ugettext_lazy as _
from django import forms
import validators

class WebsiteCreateForm(BaseForm):
    class Meta:
        model = Website
        fields = ["url", "description", "is_ready", "is_simplified"]
        labels = {
            'url': _('Adres WWW strony:'),
            'description': _('Opis:'),
            'is_ready': _('Czy aktywnya'),
            'is_simplified': _('Czy pobrane dane przetwarzać do formatu JSON (tryb zaawansowany)?'),
        }

    def clean(self):
        errors = []
        if validators.url(self.data["url"]) is not True:
            errors.append("Wprowadzony adres www został zweryfikowany jako błędny")
        if errors:
            raise forms.ValidationError(errors)

    def save(self, commit=True):
        website = Website(
            url=self.cleaned_data["url"],
            description=self.cleaned_data["description"],
            is_ready=self.cleaned_data["is_ready"],
            folder_id=self.cleaned_data["folder_id"],
        )
        website.save()


class WebsiteClearForm(BaseForm):
    class Meta:
        model = Website
        fields = []

    def save(self, commit=True):
        folder_id = self.cleaned_data["folder_id"]
        websites = Website.objects.filter(folder_id=folder_id)
        for website in websites:
            website.delete()


class WebsiteUpdateForm(BaseForm):
    class Meta:
        model = Website
        fields = ["url", "description", "is_ready", "is_simplified"]
        labels = {
            'url': _('Adres WWW strony:'),
            'description': _('Opis:'),
            'is_ready': _('Czy aktywna?'),
            'is_simplified': _('Czy pobrane dane przetwarzać do formatu JSON (tryb zaawansowany)?'),
        }