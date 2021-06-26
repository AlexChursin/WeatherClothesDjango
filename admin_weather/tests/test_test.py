import os

import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    c = User.objects.count()
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    assert  User.objects.count() > c, 'User created'