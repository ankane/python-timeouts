from .conftest import TestTimeouts
from http.client import HTTPConnection
import socket


class TestSocket(TestTimeouts):
    def test_connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        with self.raises(socket.timeout):
            s.connect((self.connect_host(), 80))

    def test_read(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((self.read_host(), self.read_port()))
        with self.raises(socket.timeout):
            s.recv(1024)
