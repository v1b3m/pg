        migrations = [name for app, name in loader.disk_migrations if app == 'migrations']
        self.assertEqual(migrations, ['0001_initial'])


class PycLoaderTests(MigrationTestBase):
