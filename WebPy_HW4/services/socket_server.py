import socket
from typing import Dict, Tuple
from urllib import parse


def socket_server(host: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        address: tuple[str, int] = host, port
        sock.bind(address)
        try:
            while True:
                data, address = sock.recvfrom(1024)
                print(f'Received data: {data.decode()} from: {address}')
                sock.sendto(data, address)
                print(f'Send data: {data.decode()} to: {address}')

        except KeyboardInterrupt:
            print('The process is done')
        finally:
            sock.close()

#
# if __name__ == '__main__':
#     host = "127.0.0.1"
#     port = 8000
#     socket_server(host, port)
