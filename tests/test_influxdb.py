from .conftest import TestTimeouts
from influxdb import InfluxDBClient
from requests.exceptions import ConnectTimeout, ReadTimeout


class TestInfluxdb(TestTimeouts):
    def test_connect(self):
        # retries=1 means one attempt
        client = InfluxDBClient(host=self.connect_host(), timeout=1, retries=1)
        with self.raises(ConnectTimeout):
            client.query('SELECT 1')

    def test_read(self):
        # retries=1 means one attempt
        client = InfluxDBClient(host=self.read_host(), port=self.read_port(), timeout=1, retries=1)
        with self.raises(ReadTimeout):
            client.query('SELECT 1')
