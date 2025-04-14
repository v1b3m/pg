@@ -138,3 +138,29 @@ class TestGetUser(TestCase):
        user = get_user(request)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, created_user.username)

    def test_session_auth_hash_secret_key_fallbacks(self):
        # Create a user
        u = User.objects.create_user("rotate", "rotate@example.com", "rotpwd")
        # Simulate login with old secret
        with self.settings(SECRET_KEY="oldsecret", SECRET_KEY_FALLBACKS=[]):
            self.client.login(username="rotate", password="rotpwd")
            session = self.client.session
            h = session.get("_auth_user_hash")
            # Compute expected salted_hmac with oldsecret
            from django.utils.crypto import salted_hmac
            key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
            expected = salted_hmac(key_salt, u.password, secret="oldsecret", algorithm="sha256").hexdigest()
            self.assertEqual(h, expected)
        # New secret with fallback oldsecret
        with self.settings(SECRET_KEY="newsecret", SECRET_KEY_FALLBACKS=["oldsecret"]):
            request = HttpRequest()
            request.session = self.client.session
            user = get_user(request)
            self.assertEqual(user, u)
            # Session hash updated to new secret
            new_hash = request.session.get("_auth_user_hash")
            expected_new = salted_hmac(key_salt, u.password, secret="newsecret", algorithm="sha256").hexdigest()
            self.assertEqual(new_hash, expected_new)
            # Save session modifications to persist
            request.session.save()