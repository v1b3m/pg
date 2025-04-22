    def settings_to_cmd_args_env(cls, settings_dict, parameters):
        args = [cls.executable_name]
        env = None
        db = settings_dict['OPTIONS'].get('db', settings_dict['NAME'])
        user = settings_dict['OPTIONS'].get('user', settings_dict['USER'])
        password = settings_dict['OPTIONS'].get(
            'password',
            args += ["--ssl-key=%s" % client_key]
        if charset:
            args += ['--default-character-set=%s' % charset]
        if db:
            args += [db]
        args.extend(parameters)
        return args, env