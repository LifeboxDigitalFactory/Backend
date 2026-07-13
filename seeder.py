#!/usr/bin/env python
"""Seed demo users for local development."""
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "academy.settings")
django.setup()

from utils import model_factories  # noqa: E402


def run():
    org = model_factories.create_organization(name="Lifebox Demo")
    model_factories.create_admin(
        organization=org,
        email="admin@lifebox.test",
        first_name="Admin",
        last_name="Lifebox",
        password="password123",
    )
    model_factories.create_collaborator(
        organization=org,
        email="colaborador1@lifebox.test",
        first_name="Ana",
        last_name="Colaboradora",
        password="password123",
    )
    model_factories.create_collaborator(
        organization=org,
        email="colaborador2@lifebox.test",
        first_name="Bruno",
        last_name="Colaborador",
        password="password123",
    )
    print("Seeder OK")
    print("  admin@lifebox.test / password123")
    print("  colaborador1@lifebox.test / password123")
    print("  colaborador2@lifebox.test / password123")


if __name__ == "__main__":
    run()
