from .conftest import TestTimeouts
from urllib.request import Request, urlopen
from urllib.error import URLError


class TestRequests(TestTimeouts):
    def test_urlopen(self):
        with self.raises(URLError):
            req = Request(self.connect_url())
            urlopen(req, timeout=1)
