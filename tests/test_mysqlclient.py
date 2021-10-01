from .conftest import TestTimeouts
import MySQLdb
from MySQLdb._exceptions import OperationalError


class TestMysqlclient(TestTimeouts):
    def test_connect(self):
        with self.raises(OperationalError):
            MySQLdb.connect(host=self.connect_host(), connect_timeout=1)

    def test_read(self):
        with self.raises(OperationalError):
            MySQLdb.connect(host=self.read_host(), port=self.read_port(), connect_timeout=1)
