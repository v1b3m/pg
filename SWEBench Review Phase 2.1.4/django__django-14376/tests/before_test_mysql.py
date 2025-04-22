            'optiondbname',
        ]
        expected_env = {'MYSQL_PWD': 'optionpassword'}
        self.assertEqual(
            self.settings_to_cmd_args_env({
                'NAME': 'settingdbname',
                'USER': 'settinguser',
                'PASSWORD': 'settingpassword',
                'HOST': 'settinghost',
                'PORT': settings_port,
                'OPTIONS': {
                    'db': 'optiondbname',
                    'user': 'optionuser',
                    'passwd': 'optionpassword',
                    'host': 'optionhost',
                    'port': options_port,
                },
            }),
            (expected_args, expected_env),
        )

    def test_options_password(self):
        expected_args = [
            'mysql',
            '--user=someuser',
            '--host=somehost',
            '--port=444',
            'somedbname',
        ]
        expected_env = {'MYSQL_PWD': 'optionpassword'}
        self.assertEqual(
            self.settings_to_cmd_args_env({
                'NAME': 'somedbname',
                'USER': 'someuser',
                'PASSWORD': 'settingpassword',
                'HOST': 'somehost',
                'PORT': 444,
                'OPTIONS': {'password': 'optionpassword'},
            }),
            (expected_args, expected_env),
        )