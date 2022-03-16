from django.db import models
from django.utils.translation import gettext_lazy as _
from scrapper.settings import APP_LABEL

from scrapper.models.utils.base import BaseModel
from scrapper.models.folder import Folder

class Website(BaseModel):
    class Meta:
        app_label = APP_LABEL
        ordering = ("pk",)

    url = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    is_ready = models.BooleanField(default=False)
    folder_id = models.ForeignKey(to=Folder, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name={self.url}, counter={self.is_ready})"

    __repr__ = __str__