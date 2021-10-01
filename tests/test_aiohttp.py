from .conftest import TestTimeouts
import aiohttp
import pytest
from asyncio.exceptions import TimeoutError


class TestAiohttp(TestTimeouts):
    @pytest.mark.asyncio
    async def test_connect(self):
        with self.raises(TimeoutError):
            timeout = aiohttp.ClientTimeout(total=1)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(self.connect_url()) as resp:
                        await resp.text()

    @pytest.mark.asyncio
    async def test_read(self):
        with self.raises(TimeoutError):
            timeout = aiohttp.ClientTimeout(total=1)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(self.read_url()) as resp:
                        await resp.text()
