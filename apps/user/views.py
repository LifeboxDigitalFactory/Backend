from django.contrib.auth import authenticate
from knox.models import AuthToken
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    organization_id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "role",
            "organization_id",
        ]

    def get_full_name(self, obj):
        return obj.full_name

    def get_role(self, obj):
        if hasattr(obj, "admin_profile"):
            return "admin"
        if hasattr(obj, "collaborator_profile"):
            return "collaborator"
        return None

    def get_organization_id(self, obj):
        if hasattr(obj, "admin_profile"):
            return obj.admin_profile.organization_id
        if hasattr(obj, "collaborator_profile"):
            return obj.collaborator_profile.organization_id
        return None


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request,
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )
        if user is None:
            return Response(
                {"text": "Credenciales inválidas"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        _, token = AuthToken.objects.create(user)
        return Response(
            {
                "token": token,
                "user": UserSerializer(user).data,
            }
        )


class VerifyTokenView(APIView):
    def post(self, request):
        return Response({"user": UserSerializer(request.user).data})


class MeView(APIView):
    def get(self, request):
        return Response(UserSerializer(request.user).data)
