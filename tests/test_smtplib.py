from .conftest import TestTimeouts
from smtplib import SMTP, SMTPServerDisconnected
from socket import timeout


class TestSmtplib(TestTimeouts):
    def test_connect(self):
        with self.raises(timeout):
            with SMTP(self.connect_host(), timeout=1) as smtp:
                smtp.noop()

    def test_read(self):
        with self.raises(SMTPServerDisconnected):
            with SMTP(self.read_host(), self.read_port(), timeout=1) as smtp:
                smtp.noop()
