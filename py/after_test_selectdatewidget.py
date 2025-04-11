import sys
from datetime import date

from django.forms import DateField, Form, SelectDateWidget
            ((None, "12", "1"), None),
            (("2000", None, "1"), None),
            (("2000", "12", None), None),
            ((str(sys.maxsize + 1), "12", "1"), "0-0-0"),
        ]
        for values, expected in tests:
            with self.subTest(values=values):