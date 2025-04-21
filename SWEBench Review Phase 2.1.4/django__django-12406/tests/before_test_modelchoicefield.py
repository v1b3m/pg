        Category.objects.all().delete()
        self.assertIs(bool(f.choices), True)

    def test_deepcopies_widget(self):
        class ModelChoiceForm(forms.Form):
            category = forms.ModelChoiceField(Category.objects.all())