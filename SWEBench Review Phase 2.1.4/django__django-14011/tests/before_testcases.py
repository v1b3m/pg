        finally:
            connections.close_all()

    def _create_server(self):
        return self.server_class(
            (self.host, self.port),
            QuietWSGIRequestHandler,
            allow_reuse_address=False,
        )

    def terminate(self):
        return cls.host

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        connections_override = {}
        for conn in connections.all():
            # If using in-memory sqlite databases, pass the connections to
            # the server thread.
            if conn.vendor == 'sqlite' and conn.is_in_memory_db():
                # Explicitly enable thread-shareability for this connection
                conn.inc_thread_sharing()
                connections_override[conn.alias] = conn

        cls._live_server_modified_settings = modify_settings(
            ALLOWED_HOSTS={'append': cls.allowed_host},
        )
        cls._live_server_modified_settings.enable()
        cls.server_thread = cls._create_server_thread(connections_override)
        cls.server_thread.daemon = True
        cls.server_thread.start()
    def _tearDownClassInternal(cls):
        # Terminate the live server's thread.
        cls.server_thread.terminate()
        # Restore sqlite in-memory database connections' non-shareability.
        for conn in cls.server_thread.connections_override.values():
            conn.dec_thread_sharing()
