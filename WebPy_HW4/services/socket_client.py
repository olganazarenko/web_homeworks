import socket
import json


def socket_client(host: str, port: int, data: object = None) -> object:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        server = host, port
        data = json.dumps(data).encode()
        client.sendto(data, server)
        print(f'Send data: {data.decode()} to server: {server}')
        data, address = client.recvfrom(1024)
        print(f'Response data: {response.decode()} from address: {address}')
    client.close()
    return data

#
# if __name__ == '__main__':
#     data = "today"
#     socket_client(ip_address, socket_port, data)
