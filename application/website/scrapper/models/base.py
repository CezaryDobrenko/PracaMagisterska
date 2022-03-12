import re
from copy import deepcopy

from django.db import models
from django.utils import timezone


def camel_to_snake(name: str) -> str:
    first_cap_re = re.compile("(.)([A-Z][a-z]+)")
    all_cap_re = re.compile("([a-z0-9])([A-Z])")
    s1 = first_cap_re.sub(r"\1_\2", name)
    return all_cap_re.sub(r"\1_\2", s1).lower()


class GrapheneMixin:
    @property
    def gid(self) -> str:
        try:
            from graphql_relay import to_global_id
        except ImportError:
            return None

        return to_global_id(f"{self.__class__.__name__}Node", self.id)

    @classmethod
    def retrieve_id(cls, gid) -> int:
        try:
            from graphql_relay import from_global_id

            object_type, object_id = from_global_id(gid)
            if object_type != f"{cls.__name__}Node":
                raise ValueError(
                    f"Passed ID [{object_type}] does not belong to class: {cls.__name__}Node"
                )
            return int(object_id)
        except ImportError:
            raise


class BaseModel(models.Model, GrapheneMixin):
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id})"

    __str__ = __repr__

    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if hasattr(self, camel_to_snake(key)):
                setattr(self, camel_to_snake(key), value)
        self.save()

    def copy_instance(self, **kwargs):
        new_instance = deepcopy(self)
        new_instance.pk = None
        new_instance.update(**kwargs)
        return new_instance
