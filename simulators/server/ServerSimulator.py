import threading

from models.Client import Client
from models.Server import Server

server: Server = Server('localhost', 6069)


def print_receive(client, addr: tuple[str, int]) -> None:
    print(f'client {addr} sent: {server.receive(client)}')


def start():
    while True:
        [client, addr] = server.accept()
        print(f'client connected {addr}\n')
        threading.Thread(target=print_receive, args=(client, addr)).start()
