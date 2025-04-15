@@ -756,13 +756,9 @@ class SessionMiddlewareTests(TestCase):
        # The cookie was deleted, not recreated.
        # A deleted cookie header looks like:
        #  Set-Cookie: sessionid=; expires=Thu, 01 Jan 1970 00:00:00 GMT; Max-Age=0; Path=/
        # The deletion cookie should include HttpOnly and SameSite attributes when appropriate.
        expected_str = 'Set-Cookie: {}=""; expires=Thu, 01 Jan 1970 00:00:00 GMT; HttpOnly; Max-Age=0; Path=/; SameSite=Lax'.format(settings.SESSION_COOKIE_NAME)
        self.assertEqual(expected_str, str(response.cookies[settings.SESSION_COOKIE_NAME]))
        # SessionMiddleware sets 'Vary: Cookie' to prevent the 'Set-Cookie'
        # from being cached.
        self.assertEqual(response['Vary'], 'Cookie')
@@ -787,13 +783,8 @@ class SessionMiddlewareTests(TestCase):
        #  Set-Cookie: sessionid=; Domain=.example.local;
        #              expires=Thu, 01 Jan 1970 00:00:00 GMT; Max-Age=0;
        #              Path=/example/
        expected_str = 'Set-Cookie: {}=""; Domain=.example.local; expires=Thu, 01 Jan 1970 00:00:00 GMT; HttpOnly; Max-Age=0; Path=/example/; SameSite=Lax'.format(settings.SESSION_COOKIE_NAME)
        self.assertEqual(expected_str, str(response.cookies[settings.SESSION_COOKIE_NAME]))

    def test_flush_empty_without_session_cookie_doesnt_set_cookie(self):
        def response_ending_session(request):