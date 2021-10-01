from .conftest import TestTimeouts
from mongoengine import connect
from pymongo.errors import ServerSelectionTimeoutError


class TestMongoEngine(TestTimeouts):
    def test_connect(self):
        with self.raises(ServerSelectionTimeoutError):
            connect(alias='connect', host=self.connect_host(), serverSelectionTimeoutMS=1000).testdb.artists.count_documents({})

    def test_read(self):
        with self.raises(ServerSelectionTimeoutError):
            connect(alias='read', host=self.read_host(), port=self.read_port(), serverSelectionTimeoutMS=1000).testdb.artists.count_documents({})
