from .conftest import TestTimeouts
import requests
from requests.exceptions import ConnectTimeout, ReadTimeout


class TestRequests(TestTimeouts):
    def test_connect(self):
        with self.raises(ConnectTimeout):
            requests.get(self.connect_url(), timeout=1)

    def test_read(self):
        with self.raises(ReadTimeout):
            requests.get(self.read_url(), timeout=1)
