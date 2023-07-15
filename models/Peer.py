from models.Client import Client
from models.Server import Server


class Peer:
    def __init__(self, server: Server, client: Client = None, root=False):
        self.__server = server
        self.__client = client
        self.__root = root

    def send(self, message: str) -> None:
        return self.__client.get_socket().send(message.encode())

    def receive(self):
        [sock, address] = self.__server.get_socket().accept()
        return sock.recv(1024)

