from .conftest import TestTimeouts
from elasticsearch import Elasticsearch
from elastic_transport import ConnectionTimeout


class TestElasticsearch(TestTimeouts):
    def test_connect(self):
        with self.raises(ConnectionTimeout):
            Elasticsearch(self.connect_url() + str(":80"), request_timeout=1).cluster.health()

    def test_read(self):
        with self.raises(ConnectionTimeout):
            Elasticsearch(self.read_url(), request_timeout=1).cluster.health()
