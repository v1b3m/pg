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

        temp_pgpass = None
        sigint_handler = signal.getsignal(signal.SIGINT)
        try:
            if passwd:
                # Create temporary .pgpass file.
                temp_pgpass = NamedTemporaryFile(mode='w+')
                try:
                    print(
                        _escape_pgpass(host) or '*',
                        str(port) or '*',
                        _escape_pgpass(dbname) or '*',
                        _escape_pgpass(user) or '*',
                        _escape_pgpass(passwd),
                        file=temp_pgpass,
                        sep=':',
                        flush=True,
                    )
                    os.environ['PGPASSFILE'] = temp_pgpass.name
                except UnicodeEncodeError:
                    # If the current locale can't encode the data, let the
                    # user input the password manually.
                    pass
            # Allow SIGINT to pass to psql to abort queries.
            signal.signal(signal.SIGINT, signal.SIG_IGN)
            subprocess.check_call(args)
        finally:
            # Restore the original SIGINT handler.
            signal.signal(signal.SIGINT, sigint_handler)
            if temp_pgpass:
                temp_pgpass.close()
                if 'PGPASSFILE' in os.environ:  # unit tests need cleanup
                    del os.environ['PGPASSFILE']

    def runshell(self):
        DatabaseClient.runshell_db(self.connection.get_connection_params())