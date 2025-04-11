@@ -176,6 +176,23 @@ def test_null_display_for_field(self):
        display_value = display_for_field(None, models.FloatField(), self.empty_value)
        self.assertEqual(display_value, self.empty_value)

    def test_number_formats_display_for_field(self):
        display_value = display_for_field(12345.6789, models.FloatField(), self.empty_value)
        self.assertEqual(display_value, '12345.6789')