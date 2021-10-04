from .conftest import TestTimeouts
import psycopg2
from psycopg2 import OperationalError


class TestPsycopg2(TestTimeouts):
    def test_connect(self):
        # TODO debug extra time
        with self.raises(OperationalError, timeout=2):
            psycopg2.connect(host=self.connect_host(), connect_timeout=1)

    def test_read(self):
        # TODO debug extra time
        with self.raises(OperationalError, timeout=2):
            psycopg2.connect(host=self.read_host(), port=self.read_port(), connect_timeout=1)
