from .conftest import TestTimeouts
import urllib3
from urllib3.exceptions import MaxRetryError


class TestUrllib3(TestTimeouts):
    def test_connect_pool_manager(self):
        http = urllib3.PoolManager(timeout=urllib3.Timeout(connect=1), retries=0)
        with self.raises(MaxRetryError):
            http.request('GET', self.connect_url())

    def test_read_pool_manager(self):
        http = urllib3.PoolManager(timeout=urllib3.Timeout(read=1), retries=0)
        with self.raises(MaxRetryError):
            http.request('GET', self.read_url())

    def test_connect_request(self):
        http = urllib3.PoolManager()
        with self.raises(MaxRetryError):
            http.request('GET', self.connect_url(), timeout=urllib3.Timeout(connect=1), retries=0)

    def test_read_request(self):
        http = urllib3.PoolManager()
        with self.raises(MaxRetryError):
            http.request('GET', self.read_url(), timeout=urllib3.Timeout(read=1), retries=0)
