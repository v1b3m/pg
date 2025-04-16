@@ -21,6 +21,8 @@ class BaseDatabaseClient:

    def runshell(self, parameters):
        args, env = self.settings_to_cmd_args_env(self.connection.settings_dict, parameters)
        if env is not None:
            # Merge with os.environ regardless of whether env is empty or not
            env = {**os.environ, **env}
        # If env is None, subprocess.run will inherit the current environment
        subprocess.run(args, env=env, check=True)