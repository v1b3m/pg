from django.db import connection
from django.db.backends.base.client import BaseDatabaseClient
from django.test import SimpleTestCase
        )
        with self.assertRaisesMessage(NotImplementedError, msg):
            self.client.settings_to_cmd_args_env(None, None)