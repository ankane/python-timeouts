from .conftest import TestTimeouts
import httpx
from httpx import ConnectTimeout, ReadTimeout


class TestHttpx(TestTimeouts):
    def test_connect(self):
        with self.raises(ConnectTimeout):
            httpx.get(self.connect_url(), timeout=1)

    def test_read(self):
        with self.raises(ReadTimeout):
            httpx.get(self.read_url(), timeout=1)

    def test_connect_client(self):
        with self.raises(ConnectTimeout):
            with httpx.Client(timeout=1) as client:
                client.get(self.connect_url())

    def test_read_client(self):
        with self.raises(ReadTimeout):
            with httpx.Client(timeout=1) as client:
                client.get(self.read_url())
