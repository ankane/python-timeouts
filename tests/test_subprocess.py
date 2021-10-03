from .conftest import TestTimeouts
from subprocess import run, TimeoutExpired


class TestSubprocess(TestTimeouts):
    def test_timeout(self):
        with self.raises(TimeoutExpired):
            run('sleep 10', shell=True, timeout=1)
