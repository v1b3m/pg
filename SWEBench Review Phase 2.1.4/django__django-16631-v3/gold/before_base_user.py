import unicodedata
import warnings

from django.contrib.auth import password_validation
from django.contrib.auth.hashers import (
    check_password,
        """
        Return an HMAC of the password field.
        """
        key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
        return salted_hmac(
            key_salt,
            self.password,
            algorithm="sha256",
        ).hexdigest()
