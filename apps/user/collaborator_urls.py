from django.urls import path

from apps.user.collaborator_views import CollaboratorListView

urlpatterns = [
    path("", CollaboratorListView.as_view(), name="collaborator-list"),
]
