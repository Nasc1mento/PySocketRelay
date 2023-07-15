import socket
from data_structures import Graph
from models.Client import Client


class Tracker:

    def __init__(self, host: str, port: int):
        self.__host: str = host
        self.__port: int = port
        self.__socket: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((self.__host, self.__port))
        self.__socket.listen()
        self.__clients: Graph = Graph.Graph()

    def add_client(self, client: Client) -> Client:
        return self.__clients.add_node(client).get_key()

    def pair_clients(self, client1: Client, client2: Client) -> None:
        return self.__clients.add_edge(client1, client2)

    def get_clients(self) -> list:
        return self.__clients.get_nodes()
