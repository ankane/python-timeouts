from .conftest import TestTimeouts
from cassandra.cluster import Cluster
from cassandra.cluster import NoHostAvailable


class TestCassandraDriver(TestTimeouts):
    def test_connect(self):
        with self.raises(NoHostAvailable):
            Cluster([self.connect_host()], connect_timeout=1).connect()

    # TODO
    # def test_read(self):
    #     Cluster([self.read_host()], port=self.read_port()).connect()
