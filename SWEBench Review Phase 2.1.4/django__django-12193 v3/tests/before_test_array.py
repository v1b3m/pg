            }
        )

    def test_render(self):
        self.check_html(
            SplitArrayWidget(forms.TextInput(), size=2), 'array', None,