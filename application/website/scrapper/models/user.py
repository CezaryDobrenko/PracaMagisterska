from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from scrapper.settings import APP_LABEL

from scrapper.models.utils.base import BaseModel
from scrapper.models.utils.graphql_mixin import GrapheneMixin

class User(AbstractUser, GrapheneMixin):
    class Meta:
        app_label = APP_LABEL
        ordering = ("pk",)

    username = models.CharField(max_length=150)
    email = models.EmailField(_("email address"), unique=True, blank=True)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name={self.email})"

    __repr__ = __str__


class Test(BaseModel):
    class Meta:
        app_label = APP_LABEL
        ordering = ("pk",)

    name = models.CharField(max_length=30)
    counter = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}, counter={self.counter})"

    __repr__ = __str__