from datetime import date, datetime

from django.core.exceptions import ValidationError
        d = GetDate({"mydate_month": "1", "mydate_day": "1", "mydate_year": "2010"})
        self.assertIn('<label for="id_mydate_month">', d.as_p())

    @translation.override("nl")
    def test_l10n_date_changed(self):
        """
            f.clean("200a-10-25")
        with self.assertRaisesMessage(ValidationError, "'Enter a valid date.'"):
            f.clean("25/10/06")
        with self.assertRaisesMessage(ValidationError, "'This field is required.'"):
            f.clean(None)
