@@ -24,6 +24,7 @@ from django.utils.translation import gettext, ngettext

from .base import Variable, VariableDoesNotExist
from .library import Library
from django.utils.functional import Promise

register = Library()

@@ -677,6 +678,13 @@ def add(value, arg):
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        # Fallback to addition of non-integers (e.g., strings).
        # If either value or arg is a lazy translation (Promise), convert both to str.
        if isinstance(value, Promise) or isinstance(arg, Promise):
            try:
                return str(value) + str(arg)
            except Exception:
                return ''
        try:
            return value + arg
        except Exception: