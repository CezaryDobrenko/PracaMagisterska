from django.db import models
from django.utils.translation import gettext_lazy as _
from scrapper.settings import APP_LABEL

from scrapper.models.utils.base import BaseModel
from scrapper.models.selectors import Selector

class CollectedData(BaseModel):
    class Meta:
        app_label = APP_LABEL
        ordering = ("pk",)

    value = models.TextField()
    selector = models.ForeignKey(to=Selector, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, value={self.value})"

    __repr__ = __str__