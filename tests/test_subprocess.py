from .conftest import TestTimeouts
from subprocess import run, TimeoutExpired


class TestSubprocess(TestTimeouts):
    def test_connect(self):
        with self.raises(TimeoutExpired):
            run('sleep 10', shell=True, timeout=1)

    def test_read(self):
        with self.raises(TimeoutExpired):
            run('sleep 10', shell=True, timeout=1)
