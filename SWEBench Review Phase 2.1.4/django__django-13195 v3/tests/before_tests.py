        #  Set-Cookie: sessionid=; expires=Thu, 01 Jan 1970 00:00:00 GMT; Max-Age=0; Path=/
        self.assertEqual(
            'Set-Cookie: {}=""; expires=Thu, 01 Jan 1970 00:00:00 GMT; '
            'Max-Age=0; Path=/'.format(
                settings.SESSION_COOKIE_NAME,
            ),
            str(response.cookies[settings.SESSION_COOKIE_NAME])
        )
        #              Path=/example/
        self.assertEqual(
            'Set-Cookie: {}=""; Domain=.example.local; expires=Thu, '
            '01 Jan 1970 00:00:00 GMT; Max-Age=0; Path=/example/'.format(
                settings.SESSION_COOKIE_NAME,
            ),
            str(response.cookies[settings.SESSION_COOKIE_NAME])
        )