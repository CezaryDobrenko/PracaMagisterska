from scrapper.models.website import Website
from scrapper.views.basic_forms import BaseForm
from scrapper.models.selectors import Selector
from django.utils.translation import ugettext_lazy as _
from django import forms

class SelectorCreateForm(BaseForm):
    class Meta:
        model = Selector
        fields = ["value", "description", "selector_type"]
        labels = {
            'value': _('Nazwa selektora:'),
            'description': _('Opis:'),
            'selector_type': _('Typ selektora:'),
        }

    def save(self, commit=True):
        selector = Selector(
            value=self.cleaned_data["value"],
            description=self.cleaned_data["description"],
            website_id=self.cleaned_data["website_id"],
            selector_type_id=self.data["selector_type"],
        )
        selector.save()


class SelectorCreateGUIForm(BaseForm):
    name = forms.CharField(label='Wybrane selectory', widget=forms.Textarea)

    class Meta:
        model = Selector
        fields = ["name"]
    
    def save(self, commit=True):
        print("-----------------------")
        print("added new selectors")
        print("-----------------------")

class SelectorApproveForm(BaseForm):
    class Meta:
        model = Selector
        fields = []

    def save(self, commit=True):
        website_id = self.cleaned_data["website_id"]
        website = Website.objects.filter(id=website_id).first()
        website.is_ready = True
        website.save()


class SelectorClearForm(BaseForm):
    class Meta:
        model = Selector
        fields = []

    def save(self, commit=True):
        website_id = self.cleaned_data["website_id"]
        selectors = Selector.objects.filter(website_id=website_id)
        for selector in selectors:
            selector.delete()


class SelectorUpdateForm(BaseForm):
    class Meta:
        model = Selector
        fields = ["value", "description", "selector_type"]
        labels = {
            'value': _('Nazwa selektora:'),
            'description': _('Opis:'),
            'selector_type': _('Typ selektora:'),
        }