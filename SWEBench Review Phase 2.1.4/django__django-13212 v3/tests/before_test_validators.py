import re
from unittest import TestCase

from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class TestFieldWithValidators(TestCase):
        form = UserForm({'full_name': 'not int nor mail'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'], ['Enter a valid integer.', 'Enter a valid email address.'])