        user = get_user(request)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, created_user.username)