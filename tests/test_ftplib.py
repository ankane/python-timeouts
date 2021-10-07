from .conftest import TestTimeouts
from ftplib import FTP
from socket import timeout


class TestFtplib(TestTimeouts):
    def test_connect(self):
        with self.raises(timeout):
            with FTP(self.connect_host(), timeout=1) as ftp:
                ftp.login()

    def test_read(self):
        with self.raises(timeout):
            with FTP(timeout=1) as ftp:
                ftp.connect(self.read_host(), self.read_port())
                ftp.login()
