from contextlib import contextmanager
import pytest
import socketserver
import threading
from time import perf_counter, sleep


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # for debugging
        # print(self.request.recv(1024))

        # TODO figure out better method
        sleep(2)


server = socketserver.TCPServer(('127.0.0.1', 4567), MyTCPHandler)
threading.Thread(target=server.serve_forever, daemon=True).start()


class UnknownTimeoutError(RuntimeError):
    pass


class TestTimeouts:
    @contextmanager
    def raises(self, exception=UnknownTimeoutError, timeout=1):
        start = perf_counter()
        with pytest.raises(exception):
            yield
        stop = perf_counter()
        assert 1 <= (stop - start) < timeout + .25

    def connect_host(self):
        return '10.255.255.1'

    def connect_url(self):
        return 'http://' + self.connect_host()

    def read_host(self):
        return '127.0.0.1'

    def read_port(self):
        return 4567

    def read_host_and_port(self):
        return self.read_host() + ':' + str(self.read_port())

    def read_url(self):
        return 'http://' + self.read_host_and_port()
