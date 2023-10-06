from .conftest import TestTimeouts
import socket
from urllib.request import Request, urlopen
from urllib.error import URLError


class TestRequests(TestTimeouts):
    def test_connect(self):
        with self.raises(URLError):
            urlopen(self.connect_url(), timeout=1)

    def test_read(self):
        with self.raises(socket.timeout):
            urlopen(self.read_url(), timeout=1)
