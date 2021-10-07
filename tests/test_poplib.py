from .conftest import TestTimeouts
from poplib import POP3
from socket import timeout


class TestPoplib(TestTimeouts):
    def test_connect(self):
        with self.raises(timeout):
            with POP3(self.connect_host(), timeout=1) as pop:
                pop.getwelcome()

    def test_read(self):
        with self.raises(timeout):
            with POP3(self.read_host(), self.read_port(), timeout=1) as pop:
                pop.getwelcome()
