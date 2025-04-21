        self.assertEqual(match.kwargs, {'pk': '1'})
        self.assertEqual(match.route, '^regex/(?P<pk>[0-9]+)/$')

    def test_path_lookup_with_inclusion(self):
        match = resolve('/included_urls/extra/something/')
        self.assertEqual(match.url_name, 'inner-extra')