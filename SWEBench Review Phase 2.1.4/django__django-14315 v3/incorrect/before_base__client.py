
    def runshell(self, parameters):
        args, env = self.settings_to_cmd_args_env(self.connection.settings_dict, parameters)
        if env:
            env = {**os.environ, **env}
        subprocess.run(args, env=env, check=True)