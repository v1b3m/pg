import errno
import os
import socket
from http.client import HTTPConnection
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen

from django.conf import settings
from django.core.servers.basehttp import WSGIServer
from django.test import LiveServerTestCase, override_settings
from django.test.testcases import LiveServerThread, QuietWSGIRequestHandler

        return urlopen(self.live_server_url + url)


class FailingLiveServerThread(LiveServerThread):
    def _create_server(self):
        raise RuntimeError('Error creating server.')