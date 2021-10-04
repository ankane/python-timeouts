from .conftest import TestTimeouts
from http.client import HTTPConnection
from socket import timeout


class TestHttp(TestTimeouts):
    def test_connect(self):
        conn = HTTPConnection(self.connect_host(), 80, timeout=1)
        with self.raises(timeout):
            conn.request('GET', '/')

    def test_read(self):
        conn = HTTPConnection(self.read_host(), self.read_port(), timeout=1)
        conn.request('GET', '/')
        with self.raises(timeout):
            conn.getresponse()
