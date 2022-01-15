from .conftest import TestTimeouts
from typesense import Client
from requests.exceptions import ConnectTimeout, ReadTimeout


class TestTypesense(TestTimeouts):
    def test_connect(self):
        client = Client({
            'api_key': 'secret',
            'nodes': [{'host': self.connect_host(), 'port': 8108, 'protocol': 'http'}],
            'connection_timeout_seconds': 1,
            'num_retries': 0,
            'retry_interval_seconds': 0
        })

        with self.raises(ConnectTimeout):
            client.collections.retrieve()

    def test_read(self):
        client = Client({
            'api_key': 'secret',
            'nodes': [{'host': self.read_host(), 'port': self.read_port(), 'protocol': 'http'}],
            'connection_timeout_seconds': 1,
            'num_retries': 0,
            'retry_interval_seconds': 0
        })

        with self.raises(ReadTimeout):
            client.collections.retrieve()
