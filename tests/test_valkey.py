from .conftest import TestTimeouts
from valkey import Valkey
from valkey.exceptions import TimeoutError


class TestValkey(TestTimeouts):
    def test_connect(self):
        with self.raises(TimeoutError):
            Valkey(host=self.connect_host(), socket_connect_timeout=1, retry=None).ping()

    def test_read(self):
        with self.raises(TimeoutError):
            Valkey(host=self.read_host(), port=self.read_port(), socket_timeout=1).ping()
