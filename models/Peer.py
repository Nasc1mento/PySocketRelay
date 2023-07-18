from models.Client import Client
from models.Server import Server


class Peer:
    def __init__(self, server: Server = None, client: Client = None, relay=True):
        self.__server = server
        self.__client = client
        self.__relay = relay

    def get_server(self) -> Server:
        return self.__server

    def get_client(self) -> Client:
        return self.__client

    def set_server(self, server: Server) -> None:
        self.__server = server

    def set_client(self, client: Client) -> None:
        self.__client = client

    def is_relay(self) -> bool:
        return self.__relay

    def close(self) -> None:
        self.__server.get_socket().close()
        self.__client.get_socket().close()

    def __str__(self) -> str:
        return f"Peer(server={self.__server}, client={self.__client})"

