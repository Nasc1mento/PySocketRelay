import socket
from data_structures import Graph
from data_structures.Edge import Edge
from models.Peer import Peer


class Tracker:

    def __init__(self, host: str, port: int):
        self.__host: str = host
        self.__port: int = port
        self.__socket: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((self.__host, self.__port))
        self.__socket.listen()
        self.__peers: Graph = Graph.Graph()

    def add_peer(self, peer: Peer) -> Peer:
        return self.__peers.add_node(peer).get_key()

    def pair_clients(self, peer1: Peer, peer2: Peer) -> Edge:
        return self.__peers.add_edge(peer1, peer2)

    def get_clients(self) -> list:
        return self.__peers.get_nodes()

    def close(self) -> None:
        self.__socket.close()