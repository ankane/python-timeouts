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
