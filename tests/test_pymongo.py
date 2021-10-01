from .conftest import TestTimeouts
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


class TestPymongo(TestTimeouts):
    def test_connect(self):
        with self.raises(ServerSelectionTimeoutError):
            MongoClient(host=self.connect_host(), serverSelectionTimeoutMS=1000).testdb.artists.count_documents({})

    def test_read(self):
        with self.raises(ServerSelectionTimeoutError):
            MongoClient(host=self.read_host(), port=self.read_port(), serverSelectionTimeoutMS=1000).testdb.artists.count_documents({})
