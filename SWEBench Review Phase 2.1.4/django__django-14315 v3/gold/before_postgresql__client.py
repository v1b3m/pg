            env['PGSSLKEY'] = str(sslkey)
        if passfile:
            env['PGPASSFILE'] = str(passfile)
        return args, env

    def runshell(self, parameters):
        sigint_handler = signal.getsignal(signal.SIGINT)