from .conftest import TestTimeouts
from telnetlib import Telnet
from socket import timeout


class TestFtplib(TestTimeouts):
    def test_connect(self):
        with self.raises(timeout):
            with Telnet(self.connect_host(), timeout=1) as tn:
                tn.read_all()

    def test_read(self):
        with self.raises(timeout):
            with Telnet(self.read_host(), self.read_port(), timeout=1) as tn:
                tn.read_all()
