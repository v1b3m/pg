            # path() URL pattern
            self.assertEqual(translate_url('/en/account/register-as-path/', 'nl'), '/nl/profiel/registreren-als-pad/')
            self.assertEqual(translation.get_language(), 'en')

        with translation.override('nl'):
            self.assertEqual(translate_url('/nl/gebruikers/', 'en'), '/en/users/')