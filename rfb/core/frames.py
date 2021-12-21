from collections import OrderedDict
from typing import NoReturn

from rfb.core.fields import Field


class BaseFrame:
    def __init__(self, data: bytes = None):
        self._payload = None

        if data:
            self.read(data)

    @property
    def payload(self) -> bytes:
        return self._payload

    def read(self, value: bytes) -> NoReturn:
        pass

    def write(self) -> bytes:
        pass


class FrameMetaclass(type):
    """
    This class is based on DeclarativeFieldsMetaclass from Django framework.
    The MRO is not traversed because I don't want to have inheritance.
    https://github.com/django/django/blob/main/django/forms/forms.py#L25
    """
    def __new__(mcs, name, bases, attrs):
        attrs['fields'] = OrderedDict()

        for key, field in attrs.items():
            if isinstance(field, Field):
                attrs['fields'][key] = field

        return super().__new__(mcs, name, bases, attrs)


class Frame(BaseFrame, metaclass=FrameMetaclass):
    pass
