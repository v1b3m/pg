
from .base import Variable, VariableDoesNotExist
from .library import Library

register = Library()

    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        try:
            return value + arg
        except Exception: