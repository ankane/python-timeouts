from .conftest import TestTimeouts
import trino
from trino.exceptions import TrinoConnectionError


class TestTrino(TestTimeouts):
    def test_connect(self):
        conn = trino.dbapi.connect(host=self.connect_host(), request_timeout=1, max_attempts=1)
        with self.raises(TrinoConnectionError):
            conn.cursor().execute('SELECT 1')

    def test_read(self):
        conn = trino.dbapi.connect(host=self.read_host(), port=self.read_port(), request_timeout=1, max_attempts=1)
        with self.raises(TrinoConnectionError):
            conn.cursor().execute('SELECT 1')

    def test_connect_tuple(self):
        conn = trino.dbapi.connect(host=self.connect_host(), request_timeout=(1, 10), max_attempts=1)
        with self.raises(TrinoConnectionError):
            conn.cursor().execute('SELECT 1')

    def test_read_tuple(self):
        conn = trino.dbapi.connect(host=self.read_host(), port=self.read_port(), request_timeout=(10, 1), max_attempts=1)
        with self.raises(TrinoConnectionError):
            conn.cursor().execute('SELECT 1')
