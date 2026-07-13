from django.contrib import admin

from apps.user.models import Admin, Collaborator, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "is_active")
    search_fields = ("email", "first_name", "last_name")


@admin.register(Admin)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "organization")


@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ("user", "organization")
