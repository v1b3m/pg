@@ -19,13 +19,11 @@ class DatabaseClient(BaseDatabaseClient):
    @classmethod
    def runshell_db(cls, conn_params):
        args = [cls.executable_name]
        host = conn_params.get('host', '')
        port = conn_params.get('port', '')
        dbname = conn_params.get('database', '')
        user = conn_params.get('user', '')
        passwd = conn_params.get('password', '')
        if user:
            args += ['-U', user]
        if host:
@@ -33,39 +31,16 @@ class DatabaseClient(BaseDatabaseClient):
        if port:
            args += ['-p', str(port)]
        args += [dbname]
        env = None
        if passwd:
            env = os.environ.copy()
            env['PGPASSWORD'] = str(passwd)
        sigint_handler = signal.getsignal(signal.SIGINT)
        try:
            signal.signal(signal.SIGINT, signal.SIG_IGN)
            subprocess.run(args, env=env, check=True)
        finally:
            signal.signal(signal.SIGINT, sigint_handler)

    def runshell(self):
        DatabaseClient.runshell_db(self.connection.get_connection_params())