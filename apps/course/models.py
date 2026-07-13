from django.db import models

from utils.base_model import BaseAbstractModel


class Course(BaseAbstractModel):
    full_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    duration_hours = models.PositiveIntegerField(default=1)
    version = models.CharField(max_length=20, default="1.0")
    organization = models.ForeignKey(
        "organization.Organization",
        on_delete=models.CASCADE,
        related_name="courses",
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.full_name} ({self.version})"
