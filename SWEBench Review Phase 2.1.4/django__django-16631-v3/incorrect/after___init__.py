@@ -5,7 +5,7 @@ from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.middleware.csrf import rotate_token
from django.utils.crypto import constant_time_compare, salted_hmac
from django.utils.module_loading import import_string
from django.views.decorators.debug import sensitive_variables

@@ -199,9 +199,22 @@ def get_user(request):
            # Verify the session
            if hasattr(user, "get_session_auth_hash"):
                session_hash = request.session.get(HASH_SESSION_KEY)
                session_hash_verified = False
                if session_hash:
                    # Compare with current secret
                    if constant_time_compare(session_hash, user.get_session_auth_hash()):
                        session_hash_verified = True
                    else:
                        # Try with fallback secrets
                        for fallback_key in getattr(settings, "SECRET_KEY_FALLBACKS", []) or []:
                            # Compute the hash for this fallback key
                            key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
                            fallback_hexdigest = salted_hmac(key_salt, user.password, secret=fallback_key, algorithm="sha256").hexdigest()
                            if constant_time_compare(session_hash, fallback_hexdigest):
                                session_hash_verified = True
                                # Update the session hash to use current secret for future verification
                                request.session[HASH_SESSION_KEY] = user.get_session_auth_hash()
                                break
                if not session_hash_verified:
                    request.session.flush()
                    user = None