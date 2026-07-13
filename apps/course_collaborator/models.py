from django.db import models

from utils.base_model import BaseAbstractModel


class CourseCollaborator(BaseAbstractModel):
    course = models.ForeignKey(
        "course.Course",
        on_delete=models.CASCADE,
        related_name="course_collaborators",
    )
    collaborator = models.ForeignKey(
        "user.Collaborator",
        on_delete=models.CASCADE,
        related_name="course_collaborators",
    )
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["course", "collaborator"],
                name="unique_course_collaborator",
            )
        ]

    def __str__(self):
        return f"{self.collaborator} -> {self.course}"
