from models.Client import Peer


class Node:

    def __init__(self, peer: Peer):
        self.__key: Peer = peer
        self.__neighbors = []

    def get_key(self):
        return self.__key

    def get_neighbors(self) -> list['Peer']:
        return self.__neighbors

    def add_neighbor(self, peer: Peer):
        node: Node = Node(peer)
        if len(self.__neighbors) == 2:
            return None
        self.__neighbors.append(node)
        return node

    def remove_neighbor(self, peer: Peer) -> None:
        self.__neighbors.remove(peer)

    def full(self) -> bool:
        return len(self.__neighbors) == 2

    def __str__(self) -> str:
        return f"Node(key={self.__key}, neighbors={self.__neighbors})"

    def __eq__(self, other: 'Node') -> bool:
        return self.__key == other.__key

    def __hash__(self) -> int:
        return hash(self.__key)
