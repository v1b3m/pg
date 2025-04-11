@@ -98,6 +98,12 @@ class FilteredRelationTests(TestCase):
            [self.author1]
        )

    def test_with_join_exclude(self):
        qs = Author.objects.annotate(
            book_alice=FilteredRelation('book', condition=Q(book__title__iexact='poem by alice')),
        ).exclude(book_alice__isnull=False)
        self.assertSequenceEqual(qs, [])

    def test_with_join_and_complex_condition(self):
        self.assertSequenceEqual(
            Author.objects.annotate(