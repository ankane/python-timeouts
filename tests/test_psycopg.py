from .conftest import TestTimeouts
import psycopg
from psycopg import OperationalError


class TestPsycopg(TestTimeouts):
    def test_connect(self):
        with self.raises(OperationalError):
            psycopg.connect(host=self.connect_host(), connect_timeout=1)

    def test_read(self):
        with self.raises(OperationalError):
            psycopg.connect(host=self.read_host(), port=self.read_port(), connect_timeout=1)
