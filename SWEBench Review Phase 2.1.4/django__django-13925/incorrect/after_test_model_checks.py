@@ -402,6 +402,20 @@ class ModelDefaultAutoFieldTests(SimpleTestCase):

        self.assertEqual(checks.run_checks(app_configs=self.apps.get_app_configs()), [])

    def test_inherited_manual_pk(self):
        class Base(models.Model):
            id = models.BigAutoField(primary_key=True)
            class Meta:
                app_label = 'check_framework.apps.CheckDefaultPKConfig'
        class Child(Base):
            class Meta:
                app_label = 'check_framework.apps.CheckDefaultPKConfig'
        # Run checks and ensure no W042 warning for child
        warnings_list = checks.run_checks(app_configs=self.apps.get_app_configs())
        # Filter any warnings with id='models.W042'
        w42 = [w for w in warnings_list if getattr(w, 'id', None) == 'models.W042' and w.obj in {Base, Child}]
        self.assertEqual(w42, [])

    def test_explicit_pk(self):
        class Model(models.Model):
            id = models.BigAutoField(primary_key=True)