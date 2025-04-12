from datetime import date

from django.forms import DateField, Form, SelectDateWidget
            ((None, "12", "1"), None),
            (("2000", None, "1"), None),
            (("2000", "12", None), None),
        ]
        for values, expected in tests:
            with self.subTest(values=values):