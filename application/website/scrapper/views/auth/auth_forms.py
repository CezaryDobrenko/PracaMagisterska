from scrapper.views.basic_forms import BaseForm
from scrapper.models.user import User
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.core.mail import send_mail

class RegisterForm(BaseForm):
    class Meta:
        model = User
        fields = []

    def clean(self):
        errors = []
        is_email_exist = User.objects.filter(email=self.data["username"]).count()
        if self.data["password"] != self.data["password2"]:
            errors.append("Podano różne hasła")
        if is_email_exist > 0:
            errors.append("Podany email już istnieje w systemie")
        if errors:
            raise forms.ValidationError(errors)

    def save(self, commit=True):
        send_mail(
            'Intresting subject',
            'Here is the message.',
            'c.dobrenko@gmail.com',
            ['cezary.dobrenko@emplocity.pl'],
            fail_silently=False,
        )
        raise ValueError()
        user = User(
            username=self.data["username"],
            email=self.data["username"],
            is_active=False,
        )
        user.set_password(self.data["password"])
        user.save()