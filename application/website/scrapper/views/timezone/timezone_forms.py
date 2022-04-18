from scrapper.views.basic_forms import BaseForm
from scrapper.models.timezone import Timezone
from scrapper.models.user import User
from django.urls import reverse
from django.http import HttpResponseRedirect

class ChangeTimezoneForm(BaseForm):
    class Meta:
        model = Timezone
        fields = []

    def save(self, id, commit=True):
        user = User.objects.get(id=id)
        user.timezone_id = self.data["timezone"]
        user.save()
        return HttpResponseRedirect(reverse('private_dashboard'))