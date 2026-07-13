from django.db import models

from utils.base_model import BaseAbstractModel


class Organization(BaseAbstractModel):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
