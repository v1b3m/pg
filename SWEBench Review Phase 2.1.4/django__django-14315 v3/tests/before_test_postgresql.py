                'PORT': '444',
            }), (
                ['psql', '-U', 'someuser', '-h', 'somehost', '-p', '444', 'dbname'],
                {},
            )
        )

    def test_parameters(self):
        self.assertEqual(
            self.settings_to_cmd_args_env({'NAME': 'dbname'}, ['--help']),
            (['psql', 'dbname', '--help'], {}),
        )

    @skipUnless(connection.vendor == 'postgresql', 'Requires a PostgreSQL connection')