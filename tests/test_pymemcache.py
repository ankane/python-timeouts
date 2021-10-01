from .conftest import TestTimeouts
from pymemcache.client.base import Client
from socket import timeout


class TestPymemcache(TestTimeouts):
    def test_connect(self):
        with self.raises(timeout):
            Client(self.connect_host(), connect_timeout=1).get('key')

    def test_read(self):
        with self.raises(timeout):
            Client(self.read_host_and_port(), timeout=1).get('key')
