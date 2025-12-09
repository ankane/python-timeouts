from .conftest import TestTimeouts
import pg8000
from pg8000.exceptions import InterfaceError
import socket


class TestPg8000(TestTimeouts):
    def test_connect(self):
        with self.raises(InterfaceError, timeout=1):
            pg8000.connect(user='', host=self.connect_host(), timeout=1)

    def test_read(self):
        with self.raises(socket.timeout, timeout=1):
            pg8000.connect(user='', host=self.read_host(), port=self.read_port(), timeout=1)
