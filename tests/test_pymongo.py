from .conftest import TestTimeouts
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


class TestPymongo(TestTimeouts):
    def test_connect(self):
        with self.raises(ServerSelectionTimeoutError):
            MongoClient(self.connect_host(), 27017, serverSelectionTimeoutMS=1000).testdb.artists.count_documents({})

    def test_read(self):
        with self.raises(ServerSelectionTimeoutError):
            MongoClient(self.read_host(), self.read_port(), serverSelectionTimeoutMS=1000).testdb.artists.count_documents({})
