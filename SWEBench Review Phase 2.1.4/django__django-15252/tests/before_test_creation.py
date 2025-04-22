@mock.patch.object(connection, 'ensure_connection')
@mock.patch.object(connection, 'prepare_database')
@mock.patch('django.db.migrations.recorder.MigrationRecorder.has_table', return_value=False)
@mock.patch('django.db.migrations.executor.MigrationExecutor.migrate')
@mock.patch('django.core.management.commands.migrate.Command.sync_apps')
class TestDbCreationTests(SimpleTestCase):
    available_apps = ['backends.base.app_unmigrated']

    def test_migrate_test_setting_false(self, mocked_sync_apps, mocked_migrate, *mocked_objects):
        test_connection = get_connection_copy()
        test_connection.settings_dict['TEST']['MIGRATE'] = False
        creation = test_connection.creation_class(test_connection)
            with mock.patch.object(creation, '_destroy_test_db'):
                creation.destroy_test_db(old_database_name, verbosity=0)

    def test_migrate_test_setting_true(self, mocked_sync_apps, mocked_migrate, *mocked_objects):
        test_connection = get_connection_copy()
        test_connection.settings_dict['TEST']['MIGRATE'] = True
        creation = test_connection.creation_class(test_connection)
                creation.destroy_test_db(old_database_name, verbosity=0)

    @mock.patch.dict(os.environ, {'RUNNING_DJANGOS_TEST_SUITE': ''})
    @mock.patch.object(BaseDatabaseCreation, 'mark_expected_failures_and_skips')
    def test_mark_expected_failures_and_skips_call(self, mark_expected_failures_and_skips, *mocked_objects):
        """