
        self.assertFalse(Child.check())

    def test_name_beginning_with_underscore(self):
        class _Model(models.Model):
            pass