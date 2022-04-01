from django import forms
from django.utils.translation import ugettext_lazy as _
from scrapper.translations.language_pl import Translator

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            field_type = visible.field.widget.__class__.__name__
            if field_type == "Select":
                visible.field.choices = self.__select_hander(visible.field)
                visible.field.widget.attrs['class'] = 'form-control'
            elif field_type == "CheckboxInput":
                visible.field.widget.attrs['class'] = 'form-control-checkbox'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    def __select_hander(self, field):
        parsed_choices = []
        for item in field.choices:
            key, value = item
            if self.__check_if_value_is_str(value):
                parsed_choices.append((key, Translator.interval_to_pl(key)))
            else:
                parsed_choices.append((key, value))
        return parsed_choices

    def __check_if_value_is_str(self, value):
        return type(value) == "str"