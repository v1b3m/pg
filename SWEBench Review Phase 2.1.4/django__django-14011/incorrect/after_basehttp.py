@@ -81,6 +81,21 @@ class ThreadedWSGIServer(socketserver.ThreadingMixIn, WSGIServer):
    """A threaded version of the WSGIServer"""
    daemon_threads = True

    def process_request_thread(self, request, client_address):
        """
        Handle a request in a new thread and ensure database connections are closed afterwards.
        """
        try:
            super().process_request_thread(request, client_address)
        finally:
            # Close any database connections opened in this thread.
            try:
                from django.db import connections
            except ImportError:
                pass
            else:
                connections.close_all()


class ServerHandler(simple_server.ServerHandler):
    http_version = '1.1'