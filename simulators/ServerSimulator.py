import threading

from models.client.Client import Client
from models.server.Server import Server

server: Server = Server('0.0.0.0', 8090)


def loop_client_receive(client: Client, addr: tuple[str, int]) -> None:
    while True:
        print(f'client {addr} sent: {server.receive(client)}')


def start():

    while True:
        [client, addr] = server.accept()
        print(f'client connected {addr}\n')
        threading.Thread(target=loop_client_receive, args=(client, addr)).start()
