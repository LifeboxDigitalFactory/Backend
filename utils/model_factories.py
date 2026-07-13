from apps.organization.models import Organization
from apps.user.models import Admin, Collaborator, User


def create_organization(**kwargs):
    defaults = {"name": "Lifebox Demo", "is_active": True}
    defaults.update(kwargs)
    name = defaults.pop("name")
    org = Organization.objects.filter(name=name).first()
    if org is None:
        org = Organization.objects.create(name=name, **defaults)
    return org


def create_user(**kwargs):
    password = kwargs.pop("password", "password123")
    defaults = {
        "email": "user@lifebox.test",
        "first_name": "Test",
        "last_name": "User",
    }
    defaults.update(kwargs)
    email = defaults.pop("email")
    user, created = User.objects.get_or_create(email=email, defaults=defaults)
    if created:
        user.set_password(password)
        user.save()
    return user


def create_admin(user=None, organization=None, **kwargs):
    if organization is None:
        organization = create_organization()
    if user is None:
        user = create_user(
            email=kwargs.pop("email", "admin@lifebox.test"),
            first_name=kwargs.pop("first_name", "Admin"),
            last_name=kwargs.pop("last_name", "Lifebox"),
            password=kwargs.pop("password", "password123"),
        )
    admin, _ = Admin.objects.get_or_create(
        user=user, defaults={"organization": organization, **kwargs}
    )
    return admin


def create_collaborator(user=None, organization=None, **kwargs):
    if organization is None:
        organization = create_organization()
    if user is None:
        user = create_user(
            email=kwargs.pop("email", "collaborator@lifebox.test"),
            first_name=kwargs.pop("first_name", "Colaborador"),
            last_name=kwargs.pop("last_name", "Uno"),
            password=kwargs.pop("password", "password123"),
        )
    collaborator, _ = Collaborator.objects.get_or_create(
        user=user, defaults={"organization": organization, **kwargs}
    )
    return collaborator
