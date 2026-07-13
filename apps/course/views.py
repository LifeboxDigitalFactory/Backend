from knox.auth import TokenAuthentication
from rest_framework import serializers
from rest_framework.generics import ListAPIView

from apps.course.models import Course
from utils.custom_permissions import IsAdmin


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "full_name",
            "description",
            "duration_hours",
            "version",
            "is_active",
            "created_at",
        ]


class CourseListView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]
    serializer_class = CourseListSerializer

    def get_queryset(self):
        organization = self.request.user.admin_profile.organization
        return Course.objects.filter(
            organization=organization,
            show=True,
        ).order_by("-created_at")
