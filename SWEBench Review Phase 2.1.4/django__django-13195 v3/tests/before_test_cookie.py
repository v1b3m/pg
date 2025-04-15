        self.assertEqual(cookie['path'], '/')
        self.assertEqual(cookie['secure'], '')
        self.assertEqual(cookie['domain'], '')

    def test_delete_cookie_secure_prefix(self):
        """
                cookie_name = '__%s-c' % prefix
                response.delete_cookie(cookie_name)
                self.assertIs(response.cookies[cookie_name]['secure'], True)