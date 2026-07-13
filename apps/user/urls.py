from django.urls import path

from apps.user.views import LoginView, MeView, VerifyTokenView

urlpatterns = [
    path("login/", LoginView.as_view(), name="user-login"),
    path("verify-token/", VerifyTokenView.as_view(), name="user-verify-token"),
    path("me/", MeView.as_view(), name="user-me"),
]
