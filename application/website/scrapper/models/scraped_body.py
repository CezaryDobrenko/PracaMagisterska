from django.db import models
from django.utils.translation import gettext_lazy as _
from scrapper.settings import APP_LABEL

from scrapper.models.utils.base import BaseModel
from scrapper.models.website import Website

class ScrapedBody(BaseModel):
    class Meta:
        app_label = APP_LABEL
        ordering = ("pk",)

    body = models.TextField()
    index = models.IntegerField()
    website = models.ForeignKey(to=Website, on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, body={self.body}, index={self.index})"

    __repr__ = __str__