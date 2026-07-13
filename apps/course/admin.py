from django.contrib import admin

from apps.course.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("full_name", "version", "organization", "is_active")
