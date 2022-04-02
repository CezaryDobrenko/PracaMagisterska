from django import forms
from django.utils.translation import ugettext_lazy as _
from scrapper.translations.language_pl import Translator

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        form_to_translate = ["FolderUpdateForm"]
        form_name = self.__class__.__name__
        for visible in self.visible_fields():
            field_type = visible.field.widget.__class__.__name__
            if field_type == "Select" and form_name in form_to_translate:
                visible.field.choices = self.__translator_hander(visible.field)
                visible.field.widget.attrs['class'] = 'form-control'
            elif field_type == "CheckboxInput":
                visible.field.widget.attrs['class'] = 'form-control-checkbox'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    def __translator_hander(self, field):
        parsed_choices = []
        for item in field.choices:
            key, _ = item
            parsed_choices.append((key, Translator.interval_to_pl(key)))
        return parsed_choices