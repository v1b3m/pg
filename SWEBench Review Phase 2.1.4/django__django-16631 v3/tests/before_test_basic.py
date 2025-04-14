from django.contrib.auth import get_user, get_user_model
from django.contrib.auth.models import AnonymousUser, User
from django.core.exceptions import ImproperlyConfigured
        user = get_user(request)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, created_user.username)