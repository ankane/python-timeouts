from .conftest import TestTimeouts
from redis import Redis
from redis.exceptions import TimeoutError


class TestRedis(TestTimeouts):
    def test_connect(self):
        with self.raises(TimeoutError):
            Redis(host=self.connect_host(), socket_connect_timeout=1, retry=None).ping()

    def test_read(self):
        with self.raises(TimeoutError):
            Redis(host=self.read_host(), port=self.read_port(), socket_timeout=1).ping()
