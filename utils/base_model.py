from django.db import models


class BaseAbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)

    class Meta:
        abstract = True
