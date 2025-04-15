@@ -836,6 +836,18 @@ class OtherModelTests(SimpleTestCase):

        self.assertFalse(Child.check())

    def test_ordering_pointing_to_related_pk(self):
        class Parent(models.Model):
            pass

        class Child(models.Model):
            parent = models.ForeignKey(Parent, models.CASCADE)

            class Meta:
                ordering = ('parent__pk',)

        self.assertFalse(Child.check())

    def test_name_beginning_with_underscore(self):
        class _Model(models.Model):
            pass