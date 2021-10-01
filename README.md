# Python Timeouts

An unresponsive service can be worse than a down one. It can tie up your entire system if not handled properly. **All network requests should have a timeout.**

Here’s how to add timeouts for popular Python packages. **[All have been tested](tests)**. The default is no timeout, unless otherwise specified. Enjoy!

[![Build Status](https://github.com/ankane/python-timeouts/workflows/build/badge.svg?branch=master)](https://github.com/ankane/python-timeouts/actions)

## Packages

- [aiohttp](#aiohttp)
- [boto3](#boto3)
- [elasticsearch](#elasticsearch)
- [opensearch-py](#opensearch-py)
- [pymemcache](#pymemcache)
- [pymongo](#pymongo)
- [psycopg2](#psycopg2)
- [redis](#redis)
- [requests](#requests)

### aiohttp

```python
timeout = aiohttp.ClientTimeout(total=1)
async with aiohttp.ClientSession(timeout=timeout) as session:
    # ...
```

Raises `asyncio.exceptions.TimeoutError`

### boto3

```python
boto3.client('s3', config=Config(connect_timeout=1, read_timeout=1))
```

Raises

- `botocore.exceptions.ConnectTimeoutError` on connect timeout
- `botocore.exceptions.ReadTimeoutError` on read timeout

### elasticsearch

```python
Elasticsearch(timeout=1)
```

Raises `elasticsearch.exceptions.ConnectionError`

### opensearch-py

```python
OpenSearch(timeout=1)
```

Raises `opensearchpy.exceptions.ConnectionError`

### psycopg2

```python
psycopg2.connect(connect_timeout=1)
```

Raises `psycopg2.OperationalError`

### pymemcache

```python
Client(host, connect_timeout=1, timeout=1)
```

Raises `socket.timeout`

### pymongo

```python
MongoClient(host, port, connectTimeoutMS=1000, socketTimeoutMS=1000, serverSelectionTimeoutMS=1000)
```

Raises `pymongo.errors.ServerSelectionTimeoutError`

### redis

```python
Redis(socket_connect_timeout=1, socket_timeout=1)
```

Raises `redis.exceptions.TimeoutError`

### requests

```python
requests.get(url, timeout=1)
```

Raises

- `requests.exceptions.ConnectTimeout` on connect timeout
- `requests.exceptions.ReadTimeout` on read timeout

## Don’t see a library you use?

[Let us know](https://github.com/ankane/python-timeouts/issues/new). Even better, [create a pull request](https://github.com/ankane/python-timeouts/pulls) for it.

## Running the Tests

```sh
git clone https://github.com/ankane/python-timeouts.git
cd python-timeouts
pip install -r requirements.txt
```

To run all tests, use:

```sh
pytest
```

To run individual tests, use:

```sh
pytest tests/test_redis.py
```
