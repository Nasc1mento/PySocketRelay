from models.Client import Client
from models.Server import Server


class Peer:
    def __init__(self, server: Server = None, client: Client = None, relay=True):
        self.__server = server
        self.__client = client
        self.__relay = relay

    def get_server(self):
        return self.__server

    def get_client(self):
        return self.__client

    def set_server(self, server: Server):
        self.__server = server

    def set_client(self, client: Client):
        self.__client = client

    def is_relay(self):
        return self.__relay

    def __str__(self):
        return f"Peer(server={self.__server}, client={self.__client})"
