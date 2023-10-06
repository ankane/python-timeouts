from .conftest import TestTimeouts
import socket
from urllib.request import Request, urlopen
from urllib.error import URLError


class TestRequests(TestTimeouts):
    def test_connect(self):
        req = Request(self.connect_url())
        with self.raises(URLError):
            urlopen(req, timeout=1)

    def test_read(self):
        req = Request(self.read_url())
        with self.raises(socket.timeout):
            urlopen(req, timeout=1)
