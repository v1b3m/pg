@@ -98,6 +98,12 @@ class FilteredRelationTests(TestCase):
            [self.author1]
        )

    def test_with_join_and_complex_condition(self):
        self.assertSequenceEqual(
            Author.objects.annotate(