from .conftest import TestTimeouts
from stripe import StripeClient, RequestsClient, APIConnectionError


class TestStripe(TestTimeouts):
    def test_connect(self):
        client = StripeClient('', base_addresses={'api': self.connect_url()}, http_client=RequestsClient(timeout=1))
        with self.raises(APIConnectionError):
            client.v1.customers.list()

    def test_read(self):
        client = StripeClient('', base_addresses={'api': self.read_url()}, http_client=RequestsClient(timeout=1))
        with self.raises(APIConnectionError):
            client.v1.customers.list()
