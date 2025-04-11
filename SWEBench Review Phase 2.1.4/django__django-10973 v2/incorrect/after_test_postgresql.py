@@ -10,24 +10,21 @@ class PostgreSqlDbshellCommandTestCase(SimpleTestCase):

    def _run_it(self, dbinfo):
        """
        Invoke runshell_db while mocking subprocess.run. Returns (args_list, pgpassword_value)
        """
        def _mock_subprocess_run(*args, **kwargs):
            self.subprocess_args = list(args[0])
            env = kwargs.get('env')
            if env and 'PGPASSWORD' in env:
                self.pgpassword = env['PGPASSWORD']
            else:
                self.pgpassword = None
            return 0
        self.subprocess_args = None
        self.pgpassword = None
        with mock.patch('subprocess.run', new=_mock_subprocess_run):
            DatabaseClient.runshell_db(dbinfo)
        return self.subprocess_args, self.pgpassword

    def test_basic(self):
        self.assertEqual(
@@ -39,7 +36,7 @@ class PostgreSqlDbshellCommandTestCase(SimpleTestCase):
                'port': '444',
            }), (
                ['psql', '-U', 'someuser', '-h', 'somehost', '-p', '444', 'dbname'],
                'somepassword',
            )
        )

@@ -66,7 +63,7 @@ class PostgreSqlDbshellCommandTestCase(SimpleTestCase):
                'port': '444',
            }), (
                ['psql', '-U', 'some:user', '-h', '::1', '-p', '444', 'dbname'],
                'some:password',
            )
        )

@@ -80,14 +77,14 @@ class PostgreSqlDbshellCommandTestCase(SimpleTestCase):
                'port': '444',
            }), (
                ['psql', '-U', 'some\\user', '-h', 'somehost', '-p', '444', 'dbname'],
                'some\\password',
            )
        )

    def test_accent(self):
        username = 'rôle'
        password = 'sésame'
        pgpass_string = password
        self.assertEqual(
            self._run_it({
                'database': 'dbname',
@@ -103,14 +100,14 @@ class PostgreSqlDbshellCommandTestCase(SimpleTestCase):

    def test_sigint_handler(self):
        """SIGINT is ignored in Python and passed to psql to abort quries."""
        def _mock_subprocess_run(*args, **kwargs):
            handler = signal.getsignal(signal.SIGINT)
            self.assertEqual(handler, signal.SIG_IGN)

        sigint_handler = signal.getsignal(signal.SIGINT)
        # The default handler isn't SIG_IGN.
        self.assertNotEqual(sigint_handler, signal.SIG_IGN)
        with mock.patch('subprocess.run', new=_mock_subprocess_run):
            DatabaseClient.runshell_db({})
        # dbshell restores the original handler.
        self.assertEqual(sigint_handler, signal.getsignal(signal.SIGINT))