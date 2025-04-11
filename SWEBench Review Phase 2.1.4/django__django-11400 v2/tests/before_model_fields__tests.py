@@ -222,9 +222,9 @@ class GetChoicesOrderingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.foo1 = Foo.objects.create(a='a', d='12.34')
        cls.foo2 = Foo.objects.create(a='b', d='12.34')
        cls.bar1 = Bar.objects.create(a=cls.foo1, b='a')
        cls.bar2 = Bar.objects.create(a=cls.foo2, b='a')
        cls.field = Bar._meta.get_field('a')

@@ -241,6 +241,14 @@ def test_get_choices(self):
            [self.foo2, self.foo1]
        )

    def test_get_choices_reverse_related_field(self):
        self.assertChoicesEqual(
            self.field.remote_field.get_choices(include_blank=False, ordering=('a',)),
@@ -250,3 +258,11 @@ def test_get_choices_reverse_related_field(self):
            self.field.remote_field.get_choices(include_blank=False, ordering=('-a',)),
            [self.bar2, self.bar1]
        )