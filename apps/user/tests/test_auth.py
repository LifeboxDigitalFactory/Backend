from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from utils import model_factories


class AuthTests(APITestCase):
    def setUp(self):
        self.org = model_factories.create_organization()
        self.admin = model_factories.create_admin(
            organization=self.org,
            email="admin@test.com",
            password="password123",
        )
        self.collaborator = model_factories.create_collaborator(
            organization=self.org,
            email="colab@test.com",
            password="password123",
        )

    def test_login_admin_success(self):
        response = self.client.post(
            reverse("user-login"),
            {"email": "admin@test.com", "password": "password123"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)
        self.assertEqual(response.data["user"]["role"], "admin")

    def test_login_invalid_credentials(self):
        response = self.client.post(
            reverse("user-login"),
            {"email": "admin@test.com", "password": "wrong"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["text"], "Credenciales inválidas")

    def test_course_list_requires_admin(self):
        login = self.client.post(
            reverse("user-login"),
            {"email": "colab@test.com", "password": "password123"},
            format="json",
        )
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {login.data['token']}")
        response = self.client.get(reverse("course-list"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
