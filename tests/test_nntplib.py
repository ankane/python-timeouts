from .conftest import TestTimeouts
from nntplib import NNTP
from socket import timeout


class TestNntplib(TestTimeouts):
    def test_connect(self):
        with self.raises(timeout):
            with NNTP(self.connect_host(), timeout=1) as nntp:
                nntp.getwelcome()

    def test_read(self):
        with self.raises(timeout):
            with NNTP(self.read_host(), self.read_port(), timeout=1) as nntp:
                nntp.getwelcome()
