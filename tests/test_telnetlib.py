from .conftest import TestTimeouts
import pytest
from socket import timeout
import sys


class TestTelnetlib(TestTimeouts):
    @pytest.mark.skipif(sys.version_info >= (3, 13), reason='removed in Python 3.13')
    def test_connect(self):
        from telnetlib import Telnet

        with self.raises(timeout):
            with Telnet(self.connect_host(), timeout=1) as tn:
                tn.read_all()

    @pytest.mark.skipif(sys.version_info >= (3, 13), reason='removed in Python 3.13')
    def test_read(self):
        from telnetlib import Telnet

        with self.raises(timeout):
            with Telnet(self.read_host(), self.read_port(), timeout=1) as tn:
                tn.read_all()
