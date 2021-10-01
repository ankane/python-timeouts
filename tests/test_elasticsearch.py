from .conftest import TestTimeouts
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError


class TestElasticsearch(TestTimeouts):
    def test_connect(self):
        with self.raises(ConnectionError):
            Elasticsearch([self.connect_url()], timeout=1).cluster.health()

    def test_read(self):
        with self.raises(ConnectionError):
            Elasticsearch([self.read_url()], timeout=1).cluster.health()
