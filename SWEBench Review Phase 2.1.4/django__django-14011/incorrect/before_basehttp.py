    """A threaded version of the WSGIServer"""
    daemon_threads = True


class ServerHandler(simple_server.ServerHandler):
    http_version = '1.1'