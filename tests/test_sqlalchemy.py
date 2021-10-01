from .conftest import TestTimeouts
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


class TestSQLAlchemy(TestTimeouts):
    def test_connect(self):
        with self.raises(OperationalError):
            create_engine('postgresql+psycopg2://' + self.connect_host() + '/dbname', connect_args={'connect_timeout': 1}).connect()

    def test_read(self):
        with self.raises(OperationalError):
            create_engine('postgresql+psycopg2://' + self.read_host_and_port() + '/dbname', connect_args={'connect_timeout': 1}).connect()
