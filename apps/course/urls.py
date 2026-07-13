from django.urls import path

from apps.course.views import CourseListView

urlpatterns = [
    path("", CourseListView.as_view(), name="course-list"),
]
