from .conftest import TestTimeouts
from imaplib import IMAP4
from socket import timeout


class TestImaplib(TestTimeouts):
    def test_connect(self):
        with self.raises(timeout):
            with IMAP4(self.connect_host(), timeout=1) as imap:
                imap.noop()

    def test_read(self):
        with self.raises(timeout):
            with IMAP4(self.read_host(), self.read_port(), timeout=1) as imap:
                imap.noop()
