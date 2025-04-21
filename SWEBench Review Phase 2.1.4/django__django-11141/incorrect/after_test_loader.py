@@ -192,10 +192,8 @@ class LoaderTests(TestCase):
    def test_load_empty_dir(self):
        with override_settings(MIGRATION_MODULES={"migrations": "migrations.faulty_migrations.namespace"}):
            loader = MigrationLoader(connection)
            # App with migrations module as a namespace package should be treated as migrated (even if empty)
            self.assertNotIn("migrations", loader.unmigrated_apps)

    @override_settings(
        INSTALLED_APPS=['migrations.migrations_test_apps.migrated_app'],