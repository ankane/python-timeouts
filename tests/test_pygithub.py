from .conftest import TestTimeouts
from github import Github
from requests.exceptions import ConnectTimeout, ReadTimeout


class TestPygithub(TestTimeouts):
    def test_connect(self):
        client = Github(base_url=self.connect_url(), timeout=1, retry=0)
        with self.raises(ConnectTimeout):
            client.get_user().name

    def test_read(self):
        client = Github(base_url=self.read_url(), timeout=1, retry=0)
        with self.raises(ReadTimeout):
            client.get_user().name
