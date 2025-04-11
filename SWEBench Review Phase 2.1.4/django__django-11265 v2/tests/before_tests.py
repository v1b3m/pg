@@ -98,6 +98,14 @@ def test_with_join(self):
            [self.author1]
        )

    def test_with_join_and_complex_condition(self):
        self.assertSequenceEqual(
            Author.objects.annotate(