from .conftest import TestTimeouts
import boto3
from botocore.config import Config
from botocore.exceptions import ConnectTimeoutError, ReadTimeoutError


class TestBoto3(TestTimeouts):
    def test_connect(self):
        config = Config(connect_timeout=1, retries={'max_attempts': 0})
        client = boto3.client('s3', config=config, endpoint_url=self.connect_url(), aws_access_key_id='akid', aws_secret_access_key='secret')
        with self.raises(ConnectTimeoutError):
            client.list_buckets()

    def test_read(self):
        config = Config(read_timeout=1, retries={'max_attempts': 0})
        client = boto3.client('s3', config=config, endpoint_url=self.read_url(), aws_access_key_id='akid', aws_secret_access_key='secret')
        with self.raises(ReadTimeoutError):
            client.list_buckets()
