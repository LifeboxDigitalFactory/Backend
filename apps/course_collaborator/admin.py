from django.contrib import admin

from apps.course_collaborator.models import CourseCollaborator


@admin.register(CourseCollaborator)
class CourseCollaboratorAdmin(admin.ModelAdmin):
    list_display = ("course", "collaborator", "assigned_at")
