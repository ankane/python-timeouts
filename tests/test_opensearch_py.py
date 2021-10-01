from .conftest import TestTimeouts
from opensearchpy import OpenSearch
from opensearchpy.exceptions import ConnectionError


class TestOpensearchPy(TestTimeouts):
    def test_connect(self):
        with self.raises(ConnectionError):
            OpenSearch([self.connect_url()], timeout=1, max_retries=0).cluster.health()

    # interferes with requests read test
    # def test_read(self):
    #     with self.raises(ConnectionError):
    #         OpenSearch([self.read_url()], timeout=1, max_retries=0).cluster.health()
