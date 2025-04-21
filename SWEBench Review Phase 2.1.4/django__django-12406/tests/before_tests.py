        award = form.save()
        self.assertIsNone(award.character)

    def test_save_blank_false_with_required_false(self):
        """
        A ModelForm with a model with a field set to blank=False and the form