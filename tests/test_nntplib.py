from .conftest import TestTimeouts
import pytest
from socket import timeout
import sys


class TestNntplib(TestTimeouts):
    @pytest.mark.skipif(sys.version_info >= (3, 13), reason='removed in Python 3.13')
    def test_connect(self):
        from nntplib import NNTP

        with self.raises(timeout):
            with NNTP(self.connect_host(), timeout=1) as nntp:
                nntp.getwelcome()

    @pytest.mark.skipif(sys.version_info >= (3, 13), reason='removed in Python 3.13')
    def test_read(self):
        from nntplib import NNTP

        with self.raises(timeout):
            with NNTP(self.read_host(), self.read_port(), timeout=1) as nntp:
                nntp.getwelcome()
