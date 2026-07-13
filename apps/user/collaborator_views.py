from knox.auth import TokenAuthentication
from rest_framework import serializers
from rest_framework.generics import ListAPIView

from apps.user.models import Collaborator
from utils.custom_permissions import IsAdmin


class CollaboratorListSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email")
    full_name = serializers.CharField(source="user.full_name")

    class Meta:
        model = Collaborator
        fields = ["id", "email", "full_name"]


class CollaboratorListView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]
    serializer_class = CollaboratorListSerializer

    def get_queryset(self):
        organization = self.request.user.admin_profile.organization
        return Collaborator.objects.filter(
            organization=organization,
            show=True,
        ).select_related("user")
