from .conftest import TestTimeouts
import asyncpg
from asyncio.exceptions import TimeoutError
import pytest


class TestAsyncpg(TestTimeouts):
    @pytest.mark.asyncio
    async def test_connect(self):
        with self.raises(TimeoutError):
            await asyncpg.connect(host=self.connect_host(), timeout=1)

    @pytest.mark.asyncio
    async def test_read(self):
        with self.raises(TimeoutError):
            await asyncpg.connect(host=self.read_host(), port=self.read_port(), timeout=1)
