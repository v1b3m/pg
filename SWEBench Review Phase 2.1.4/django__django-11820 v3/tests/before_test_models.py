            )
        ])

    def test_ordering_allows_registered_lookups(self):
        class Model(models.Model):
            test = models.CharField(max_length=100)
        with register_lookup(models.CharField, Lower):
            self.assertEqual(Model.check(), [])

    def test_ordering_pointing_to_foreignkey_field(self):
        class Parent(models.Model):
            pass