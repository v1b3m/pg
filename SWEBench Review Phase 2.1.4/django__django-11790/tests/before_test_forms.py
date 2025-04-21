        CustomEmailField.objects.create_user(**data)
        form = AuthenticationForm(None, data)
        self.assertEqual(form.fields['username'].max_length, 255)
        self.assertEqual(form.errors, {})

    @override_settings(AUTH_USER_MODEL='auth_tests.IntegerUsernameUser')
        IntegerUsernameUser.objects.create_user(**data)
        form = AuthenticationForm(None, data)
        self.assertEqual(form.fields['username'].max_length, 254)
        self.assertEqual(form.errors, {})

    def test_username_field_label(self):