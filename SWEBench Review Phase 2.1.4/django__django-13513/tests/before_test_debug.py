        self.assertIn('<p>Request data not supplied</p>', html)
        self.assertNotIn('During handling of the above exception', html)

    def test_reporting_of_nested_exceptions(self):
        request = self.rf.get('/test_view/')
        try: