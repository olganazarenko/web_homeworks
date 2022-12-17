from threading import Thread

from services.run_http import run_server
from services.socket_server import socket_server

host = "127.0.0.1"
port = 5000


if __name__ == '__main__':
    http_thread: Thread = Thread(target=run_server)
    socket_server_thread: Thread = Thread(target=socket_server, args=(host, port))
    # args = (host, port)
    http_thread.start()
    socket_server_thread.start()
    http_thread.join()
    socket_server_thread.join()
