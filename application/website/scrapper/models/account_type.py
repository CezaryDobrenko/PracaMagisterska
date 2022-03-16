from django.db import models
from django.utils.translation import gettext_lazy as _
from scrapper.settings import APP_LABEL

from scrapper.models.utils.base import BaseModel
from scrapper.models.user import User
from scrapper.models.utils.levels import Level

class AccountType(BaseModel):
    class Meta:
        app_label = APP_LABEL
        ordering = ("pk",)

    name = models.CharField(max_length=200)
    scraping_interval = models.CharField(
        max_length=20, choices=Level.Options.choices, default=Level.Options.FREE
    )
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}, counter={self.is_ready})"

    __repr__ = __str__